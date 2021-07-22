#!/usr/bin/env python3

""" task 1-async comprehension """

from asyncio import sleep
from random import uniform
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """  The coroutine will collect 10 random numbers
    using an async comprehensing over async_generator,
    then return the 10 random numbers. """
    a = [i async for i in async_generator()]
    return a
