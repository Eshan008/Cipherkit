import json
import os
from datetime import datetime

#Json file creation
hist_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "history.json")

def _load_raw():
    if not os.path.exists(hist_file):
        return []
    try:
        with open(hist_file, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, OSError):
        return []

#json file entries
def logs(cipher, mode, key, input_text, output_text):
    history = _load_raw()
    entry = {"timestamp": datetime.now().isoformat(timespec="seconds"),"cipher": cipher,"mode": mode,"key": key,"input": input_text,"output": output_text,}
    history.append(entry)
    with open(hist_file, "w", encoding="utf-8") as f:
        json.dump(history, f, indent=2)
def get_history():
    return _load_raw()
def clr_hist():
    with open(hist_file, "w", encoding="utf-8") as f:
        json.dump([], f)