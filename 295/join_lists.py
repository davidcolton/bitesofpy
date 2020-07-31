from typing import List, Union
from itertools import chain


def join_lists(lst_of_lst: List[List[str]], sep: str) -> Union[List[str], None]:
    return (
        list(chain(*[x if idx == 0 else [sep] + x for idx, x in enumerate(lst_of_lst)]))
        if lst_of_lst
        else None
    )
