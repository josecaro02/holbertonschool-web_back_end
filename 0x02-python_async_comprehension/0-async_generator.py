#!/usr/bin/env python3

""" task 0 async generator """

from asyncio import sleep
from random import uniform
from typing import AsyncGenerator, Generator


async def async_generator() -> Generator[float, None, None]:
    """coroutine called async_generator that takes no arguments.
    The coroutine will loop 10 times, each time asynchronously wait 1 second,
    then yield a random number between 0 and 10"""
    for _ in range(10):
        await sleep(1)
        yield uniform(0, 10)
