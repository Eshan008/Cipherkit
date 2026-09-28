from typing import Union
#main shilfting function
def shift_char(ch: str, shift: int) -> str:
    if ch.isupper():
        base = ord('A')
        return chr((ord(ch) - base + shift) % 26 + base)
    if ch.islower():
        base = ord('a')
        return chr((ord(ch) - base + shift) % 26 + base)
    return ch

def encrypt(plaintext: str, key: Union[int, str]) -> str:
    shift = validate_key(key)
    return ''.join(shift_char(ch, shift) for ch in plaintext)

def decrypt(ciphertext: str, key: Union[int, str]) -> str:
    shift = validate_key(key)
    return ''.join(shift_char(ch, -shift) for ch in ciphertext)
# the shift key
def validate_key(key: Union[int, str]) -> int:
    try:
        shift = int(key)
    except (TypeError, ValueError):
        raise ValueError("Caesar cipher key must be an integer")
    return shift % 26
