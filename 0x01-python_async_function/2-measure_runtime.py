#!/usr/bin/env python3
""" Task measure_runtime """

from asyncio import run
from time import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """  function with integers n and max_delay as arguments that
    measures the total execution time for wait_n(n, max_delay),
    and returns total_time.
    meauser_time function should return a float. """
    start = time()

    run(wait_n(n, max_delay))

    end = time()

    return (end - start) / n
