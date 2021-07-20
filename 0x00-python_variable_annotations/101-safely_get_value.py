#!/usr/bin/env python3
""" task safety get value from python variable annotations project"""
from typing import Mapping, Any, Sequence, Union, TypeVar


T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """ Safely get value function  with type annotations"""
    if key in dct:
        return dct[key]
    else:
        return default
