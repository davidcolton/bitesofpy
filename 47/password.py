import string
import re

PUNCTUATION_CHARS = list(string.punctuation)

used_passwords = set("PassWord@1 PyBit$s9".split())


def validate_password(password):
    if (
        (6 <= len(password) <= 12)
        and (bool(re.search(r"\d", password)))
        and (len(re.findall(r"[a-z]", password)) >= 2)
        and (bool(re.search(r"[A-Z]", password)))
        and (any([x in PUNCTUATION_CHARS for x in password]))
        and (not password in used_passwords)
    ):
        used_passwords.add(password)
        return True
    else:
        return False
