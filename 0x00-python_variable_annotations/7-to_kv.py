#!/usr/bin/env python3
""" Task to_kv from python variable annotations project"""
from typing import Callable, Iterator, Union, Optional, List, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    function to_kv that takes a string k and an int OR float
    v as arguments and returns a tupla
    """
    return (k, v**2)
