import logging
import os
from gui import Cipher_kit

LOG_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "app.log")

#logging function
def set_log():
    logging.basicConfig(filename=LOG_FILE,level=logging.INFO,format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",)

def main():
    set_log()
    logging.getLogger("crypto_toolkit").info("Application starting")
    app = Cipher_kit()
    app.mainloop()
if __name__ == "__main__":
    main()
