def val_rails(key) -> int:
    try:
        rails = int(key)
    except (TypeError, ValueError):
        raise ValueError("Rail Fence key must be an integer >= 2.")
    if rails < 2:
        raise ValueError("Rail Fence key must be an integer >= 2.")
    return rails

def rail_pattern(length: int, rails: int):
    row, direction = 0, 1
    for _ in range(length):
        yield row
        if row == 0:
            direction = 1
        elif row == rails - 1:
            direction = -1
        row += direction
def encrypt(plaintext: str, key) -> str:
    rails = val_rails(key)
    fence = [[] for _ in range(rails)]
    for ch, row in zip(plaintext, rail_pattern(len(plaintext), rails)):
        fence[row].append(ch)
    return ''.join(''.join(row) for row in fence)
def decrypt(ciphertext: str, key) -> str:
    rails = val_rails(key)
    length = len(ciphertext)
    pattern = list(rail_pattern(length, rails))
    positions_per_rail = [[] for _ in range(rails)]
    for pos, row in enumerate(pattern):
        positions_per_rail[row].append(pos)
    result = [''] * length
    idx = 0
    for row in range(rails):
        for pos in positions_per_rail[row]:
            result[pos] = ciphertext[idx]
            idx += 1
    return ''.join(result)
