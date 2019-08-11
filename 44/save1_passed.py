import string
import secrets

def gen_key(parts=4, chars_per_part=8):
    key = []
    alphabet = string.ascii_uppercase + string.digits
    guard = 0
    while guard < parts:
        key.append(''.join([''.join(secrets.choice(alphabet) for _ in range(chars_per_part))]))
        key.append('-')
        guard += 1
    return(''.join(key[:-1]))
        