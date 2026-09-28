# CipherKit

A desktop cryptography toolkit built with Python and Tkinter that lets you encrypt and decrypt text using four classical ciphers (**Caesar**, **Vigenère**, **Rail Fence** and **Substitution**) through a simple tabbed GUI, with a persistent history of every operation.

## Overview

CipherKit is a hands-on learning tool for classical cryptography. Pick a cipher, enter a key, type or paste your text, and encrypt or decrypt it instantly. Every operation is timestamped and saved locally, so you can review past work from the History tab.

The project uses a modular, layered design. The GUI, cipher algorithms, input validation and history storage are separate modules, so a new cipher can be added without changing the GUI code.

## Features

- Four classical ciphers: Caesar (integer shift), Vigenère (keyword), Rail Fence (zig-zag rails), Substitution (26-letter permutation)
- Key-format hint that updates when you switch ciphers
- Encrypt, Decrypt, Clear and Copy Output buttons
- Input and key validation with clear error dialogs instead of crashes
- Persistent history of every operation (timestamp, cipher, mode, key, input, output) in `history.json`
- History tab with a detail view for each record and a "Clear history" option
- Application logging to `app.log`, separate from the user-facing history

## Technologies Used

- Python 3
- Tkinter / ttk
- `json` module for history storage
- `logging` module for application logs

## Project Structure

```
cipherkit/
├── main.py              
├── gui.py              
├── storage.py           
├── utils.py             
├── ciphers/
│   ├── __init__.py      
│   ├── caesar.py
│   ├── vigenere.py
│   ├── rail_fence.py
│   └── substitution.py
├── history.json         
├── app.log             
├── README.md
└── statement.md
```

## Installation and Running

1. Install **Python 3.8+**. Tkinter ships with the standard installer on Windows and macOS. On Linux you may need `sudo apt install python3-tk`.
2. Clone the repository:
   ```bash
   git clone https://github.com/Eshan008/cipherkit.git
   cd cipherkit
   ```
3. No external packages are needed. The project uses only the Python standard library.
4. Run the app:
   ```bash
   python main.py
   ```

## How to Use

1. On the **Ciphers** tab, choose a cipher from the dropdown. The hint next to the Key field shows the expected key format.
2. Enter a key in that format.
3. Type or paste your text into **Input text**.
4. Click **Encrypt** or **Decrypt**. The result appears in the read-only **Output** box.
5. Use **Copy Output** to copy the result, or **Clear** to reset the workspace.
6. Open the **History** tab to see past operations. Click a row to view its full input and output, or use **Clear history** to wipe the log.

## Key Formats

| Cipher       | Key format                        |
|--------------|-----------------------------------|
| Caesar       | Integer shift (e.g. `3`)          |
| Vigenère     | Alphabetic keyword (e.g. `lemon`) |
| Rail Fence   | Integer rails ≥ 2 (e.g. `3`)      |
| Substitution | 26-letter mix of the alphabet     |

## How the Program Works

1. **Startup:** `main.py` configures logging to `app.log` and launches the `Cipher_kit` window with two tabs, Ciphers and History.
2. **Cipher selection:** choosing a cipher triggers `key_desc()`, which updates the key hint.
3. **Running a cipher:** Encrypt and Decrypt both call `_run(mode)`. It looks up the chosen module in the `CIPHERS` dictionary, checks that the input is not empty with `utils.require_non_empty()`, then calls the module's `encrypt()` or `decrypt()`.
4. **Key validation:** each cipher module validates its own key and raises a `ValueError` if it is wrong.
5. **Output:** the result is shown in the read-only output box.
6. **Logging:** `storage.logs()` appends the operation to `history.json`, and a line is written to `app.log`.
7. **Error handling:** a `ValueError` shows a error dialog. Any other exception shows a generic dialog and is logged.
8. **History:** opening the History tab reloads records from `history.json`. Selecting a row shows its details, and "Clear history" resets the file after confirmation.

## Testing

The project was tested manually for normal and edge cases in each cipher: empty input, invalid keys, round-trip encrypt then decrypt, case preservation, and non-alphabetic characters.

To add automated tests, create a `tests/` folder with `pytest` cases that check `decrypt(encrypt(text, key), key) == text` for each cipher and that invalid keys raise `ValueError`.

## Screenshots

<img width="762" height="592" alt="image" src="https://github.com/user-attachments/assets/6b822d64-7449-43f5-8e49-0c929b92f212" />
