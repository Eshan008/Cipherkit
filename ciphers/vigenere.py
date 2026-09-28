#the alphabetic key
def val_key(key: str) -> str:
    if not key or not key.isalpha():
        raise ValueError("it should be an alphabetic string")
    return key.lower()

def process(text: str, key: str, encrypting: bool) -> str:
    key = val_key(key)
    result = []
    key_index = 0
    key_len = len(key)
    for ch in text:
        if ch.isalpha():
            shift = ord(key[key_index % key_len]) - ord('a')
            if not encrypting:
                shift = -shift
            base = ord('A') if ch.isupper() else ord('a')
            new_ch = chr((ord(ch) - base + shift) % 26 + base)
            result.append(new_ch)
            key_index += 1
        else:
            result.append(ch)
    return ''.join(result)
def encrypt(plaintext: str, key: str) -> str:
    return process(plaintext, key, encrypting=True)
def decrypt(ciphertext: str, key: str) -> str:
    return process(ciphertext, key, encrypting=False)
