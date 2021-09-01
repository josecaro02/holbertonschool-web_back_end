#!/usr/bin/env python3
"""
Main file
"""
import redis
from excercise import Cache

#Cache = __import__('exercise1').Cache

cache = Cache()

data = b"hello"
key = cache.store(data)
print(key)

local_redis = redis.Redis()
print(local_redis.get(key))
