import logging
import tkinter as tk
from tkinter import ttk, messagebox

from ciphers import CIPHERS
import storage
import utils

logger = logging.getLogger("crypto_toolkit.gui")
#Main Window
class Cipher_kit(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Cipher Encryption and Decryption")
        self.geometry("760x560")
        self.minsize(640, 480)

        notebook = ttk.Notebook(self)
        notebook.pack(fill="both", expand=True, padx=8, pady=8)

        self.cipher_tab = CipherTab(notebook)
        self.history_tab = HistoryTab(notebook)

        notebook.add(self.cipher_tab, text="Ciphers")
        notebook.add(self.history_tab, text="History")

        notebook.bind("<<NotebookTabChanged>>", lambda e: self.history_tab.refresh())
#Different Tabs
class CipherTab(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent, padding=12)

        ttk.Label(self, text="Cipher:").grid(row=0, column=0, sticky="w", pady=4)
        self.cipher_var = tk.StringVar(value="Caesar")
        cipher_menu = ttk.Combobox(
            self, textvariable=self.cipher_var, values=list(CIPHERS.keys()),
            state="readonly", width=20
        )
        cipher_menu.grid(row=0, column=1, sticky="w", pady=4)
        cipher_menu.bind("<<ComboboxSelected>>", self.key_desc)

        ttk.Label(self, text="Key:").grid(row=1, column=0, sticky="w", pady=4)
        self.key_entry = ttk.Entry(self, width=30)
        self.key_entry.grid(row=1, column=1, sticky="w", pady=4)

        self.key_hint = ttk.Label(self, text="", foreground="#555555")
        self.key_hint.grid(row=1, column=2, sticky="w", padx=8)
        self.key_desc()

        ttk.Label(self, text="Input text:").grid(row=2, column=0, sticky="nw", pady=4)
        self.input_text = tk.Text(self, height=8, width=70, wrap="word")
        self.input_text.grid(row=2, column=1, columnspan=2, pady=4, sticky="w")

        btn_frame = ttk.Frame(self)
        btn_frame.grid(row=3, column=1, sticky="w", pady=8)
        ttk.Button(btn_frame, text="Encrypt", command=self._encrypt).pack(side="left", padx=4)
        ttk.Button(btn_frame, text="Decrypt", command=self._decrypt).pack(side="left", padx=4)
        ttk.Button(btn_frame, text="Clear", command=self.clear).pack(side="left", padx=4)
        ttk.Button(btn_frame, text="Copy Output", command=self.copy_output).pack(side="left", padx=4)

        ttk.Label(self, text="Output:").grid(row=4, column=0, sticky="nw", pady=4)
        self.output_text = tk.Text(self, height=8, width=70, wrap="word", state="disabled")
        self.output_text.grid(row=4, column=1, columnspan=2, pady=4, sticky="w")
#conditons for the different ciphers
    def key_desc(self, event=None):

        hints = {
            "Caesar": "integer shift",
            "Vigenere": "keyword, letters only",
            "Rail Fence": "integer rails >= 2",
            "Substitution": "26-letter alphabet mix",
        }
        self.key_hint.config(text=hints.get(self.cipher_var.get(), ""))

    def _run(self, mode):
        cipher_name = self.cipher_var.get()
        cipher_module = CIPHERS[cipher_name]
        key = self.key_entry.get().strip()
        raw_text = self.input_text.get("1.0", "end").rstrip("\n")

        try:
            utils.require_non_empty(raw_text, "Input text")

            func = cipher_module.encrypt if mode == "Encrypt" else cipher_module.decrypt
            result = func(raw_text, key)

            self.output_text.config(state="normal")
            self.output_text.delete("1.0", "end")
            self.output_text.insert("1.0", result)
            self.output_text.config(state="disabled")

            storage.logs(cipher_name, mode, key, raw_text, result)
            logger.info("%s %s using key=%s", mode, cipher_name, key)

        except ValueError as e:
            messagebox.showerror("Invalid input", str(e))
            logger.warning("Validation error: %s", e)
        except Exception as e:

            messagebox.showerror("Unexpected error", f"Something went wrong:\n{e}")
            logger.exception("Unexpected error during %s", mode)

    def _encrypt(self):
        self._run("Encrypt")

    def _decrypt(self):
        self._run("Decrypt")

    def clear(self):
        self.input_text.delete("1.0", "end")
        self.output_text.config(state="normal")
        self.output_text.delete("1.0", "end")
        self.output_text.config(state="disabled")
        self.key_entry.delete(0, "end")

    def copy_output(self):
            output = self.output_text.get("1.0", "end").rstrip("\n")
            if not output:
                messagebox.showinfo("Are You Dumb?", "Output is empty!.")
                return
            self.clipboard_clear()
            self.clipboard_append(output)
            self.update()
            
class HistoryTab(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent, padding=12)
        columns = ("timestamp", "cipher", "mode", "key")
        self.tree = ttk.Treeview(self, columns=columns, show="headings", height=15)
        for col, width in zip(columns, (150, 100, 80, 150)):
            self.tree.heading(col, text=col.capitalize())
            self.tree.column(col, width=width)
        self.tree.pack(fill="both", expand=True, pady=6)
        self.tree.bind("<<TreeviewSelect>>", self.show_details)
        self.detail_box = tk.Text(self, height=6, wrap="word", state="disabled")
        self.detail_box.pack(fill="x", pady=6)
        ttk.Button(self, text="Clear history", command=self.clear).pack(anchor="e")
        self._records = []
        self.refresh()

    def refresh(self):
        self._records = storage.get_history()
        self.tree.delete(*self.tree.get_children())
        for i, rec in enumerate(self._records):
            self.tree.insert("", "end", iid=str(i), values=(
                rec["timestamp"], rec["cipher"], rec["mode"], rec["key"]
            ))

    def show_details(self, event=None):
        selection = self.tree.selection()
        if not selection:
            return
        rec = self._records[int(selection[0])]
        content = f"Input:  {rec['input']}\nOutput: {rec['output']}"

        self.detail_box.config(state="normal")
        self.detail_box.delete("1.0", "end")
        self.detail_box.insert("1.0", content)
        self.detail_box.config(state="disabled")
#clear history window
    def clear(self):
        if messagebox.askyesno("Clear history", "YE SAB DELEATE HO JAYEGA, ARE YOU SURE?"):
            storage.clr_hist()
            self.refresh()

    