from collections import Counter


def freq_digit(num: int) -> int:
    digits = Counter(str(num))
    return int(digits.most_common(1)[0][0])
