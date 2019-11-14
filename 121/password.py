import re
import string


def _check_letters(password):
    return (
        1
        if (
            any([c in string.ascii_lowercase for c in password])
            and any([c in string.ascii_uppercase for c in password])
        )
        else 0
    )


def _check_digit(password):
    return (
        1
        if (
            any([d in string.digits for d in password])
            and any([c in string.ascii_letters for c in password])
        )
        else 0
    )


def _check_length(password):
    return 1 if len(password) >= 8 else 0


def _check_special(password):
    return 1 if any([c in string.punctuation for c in password]) else 0


def _check_repeated(password):
    if len(password) < 8:
        return 0
    else:
        return 1 if len(re.findall(r"(.)\1", password)) == 0 else 0


def password_complexity(password):
    """Input: password string, calculate score according to 5 criteria in bite,
       return: score int"""
    return sum(
        [
            _check_letters(password),
            _check_digit(password),
            _check_length(password),
            _check_special(password),
            _check_repeated(password),
        ]
    )


password_complexity("aB112345fg")

