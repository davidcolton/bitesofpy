from typing import Dict


def decompress(string: str, table: Dict[str, str]) -> str:
    if string == "":
        return ""
    if not table.keys():
        return string
    while any(k in string for k in table.keys()):
        for k, v in table.items():
            string = string.replace(k, v)
            print(string)
    return string

