#!/usr/bin/env python3
""" task safe first element from python variable annotations """
from typing import Any, Union, Sequence, Iterable, List, Tuple


# The types of the elements of the input are not know
def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """ Safe first element function with correct duck-typed annotations """
    if lst:
        return lst[0]
    else:
        return None
