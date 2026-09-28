import string

plain_alp = string.ascii_uppercase
#the substitution part
def val_key(key: str) -> str:
    if not key:
        raise ValueError("Substitution key must not be empty")
    key_upper = key.upper()
    if len(key_upper) != 26 or set(key_upper) != set(plain_alp):
        raise ValueError("Substitution key must be a 26-letter mix of the alphabet")
    return key_upper

def encrypt(plaintext: str, key: str) -> str:
    key = val_key(key)
    mapping = str.maketrans(plain_alp, key)
    lower_mapping = str.maketrans(plain_alp.lower(), key.lower())
    return plaintext.translate(mapping).translate(lower_mapping)

def decrypt(ciphertext: str, key: str) -> str:
    key = val_key(key)
    mapping = str.maketrans(key, plain_alp)
    lower_mapping = str.maketrans(key.lower(), plain_alp.lower())
    return ciphertext.translate(mapping).translate(lower_mapping)