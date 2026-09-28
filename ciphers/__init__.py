# to add more ciphers, add the py file in the CIPHERS folder and add the details below
from . import caesar, vigenere, rail_fence, substitution

CIPHERS = {
    "Caesar": caesar,
    "Vigenere": vigenere,
    "Rail Fence": rail_fence,
    "Substitution": substitution,
}

__all__ = ["CIPHERS", "caesar", "vigenere", "rail_fence", "substitution"]
