from typing import List


def jagged_list(lst_of_lst: List[List[int]], fillvalue: int = 0) -> List[List[int]]:
    if len(lst_of_lst) == 0:
        return []
    max_length = max([len(l) for l in lst_of_lst])
    padded_lst_of_lst = []
    for lst in lst_of_lst:
        padded_lst_of_lst.append(
            [
                int(n)
                for n in "".join(str(c) for c in lst).ljust(max_length, str(fillvalue))
            ]
        )
    return padded_lst_of_lst
