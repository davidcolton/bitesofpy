#!/usr/bin/env python3

# Base-62 hash

import string
import time

_BASE = 62


class HashDigest:
    """Base base 62 hash library."""

    def __init__(self):
        self.base = string.digits + string.ascii_lowercase + string.ascii_uppercase
        self.short_str = ""

    def encode(self, j):
        """Returns the repeated div mod of the number.
        :param j: int
        :return: list
        """
        if j == 0:
            return [j]
        r = []
        dividend = j
        while dividend > 0:
            dividend, remainder = divmod(dividend, _BASE)
            r.append(remainder)
        r = list(reversed(r))
        return r

    def decode(self, short_str):
        """
        :param short_str:
        :return:
        """
        # slow
        val_hash = []
        for shrt in short_str:
            print(f"shrt: {shrt}")
            val_hash.append(self.base.index(shrt))
        print(f"val_hash: {val_hash}")
        val_hash = list(reversed(val_hash))
        print(f"val_hash reversed: {val_hash}")
        _id = 0
        for idx, val in enumerate(val_hash):
            print(f"idx, val: {idx}, {val}")
            _id += val * (_BASE ** idx)
        print(f"_id: {_id}")
        return _id

    def shorten(self, i):
        """
        :param i:
        :return: str
        """
        self.short_str = ""
        encoded_list = self.encode(i)
        for val in encoded_list:
            self.short_str += self.base[val]
        return self.short_str

    def unshorten(self, s):
        """Just for shorten/unshorten naming convention."""
        return self.decode(s)


if __name__ == "__main__":
    hd = HashDigest()
    print(hd.shorten(100))
    print(hd.decode("1C"))
