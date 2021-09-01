#!/usr/bin/env python3
''' Excercise file from redis basic'''
import redis
from typing import Union
from uuid import uuid4


class Cache():
    ''' Cache class for redis'''

    def __init__(self):
        ''' init method cache class'''
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        ''' store method to save data in redis'''
        keyData = str(uuid4())
        self._redis.set(keyData, data)
        return(keyData)
