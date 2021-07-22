#!/usr/bin/env python3
""" 3-tasks task of python async function project """

from asyncio import Task, create_task

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> Task:
    """ function that takes an integer max_delay and
    returns a asyncio.Task. """
    t = create_task(wait_random(max_delay))
    return t
