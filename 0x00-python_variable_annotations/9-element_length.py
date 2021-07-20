#!/usr/bin/env python3
""" task element lenth from python variable annotations project """
from typing import Mapping, MutableMapping, Sequence, Iterable, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ Function element length with appropiate types """
    return [(i, len(i)) for i in lst]
