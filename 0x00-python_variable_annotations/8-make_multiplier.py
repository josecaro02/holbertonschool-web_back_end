#!/usr/bin/env python3
""" Task make multiplier from python variable annotations project """
from typing import Callable, Iterator, Union, Optional, List, Tuple


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    function make_multiplier that takes a float multiplier as
    argument and returns a function that multiplies a float by multiplier
    """
    def functionMultiplier(n: float) -> float:
        """ function that multiplies a float by multiplier """
        return float(n * multiplier)

    return functionMultiplier
