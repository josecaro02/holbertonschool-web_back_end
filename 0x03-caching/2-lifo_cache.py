#!/usr/bin/env python3
""" LIFo cache task"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ lifo cache class"""

    def __init__(self):
        """ overload init"""
        super().__init__()
        self.orderCache = []

    def put(self, key, item):
        """ LIFO put method"""
        if key is None or item is None:
            return

        self.cache_data[key] = item

        if len(self.cache_data.keys()) > BaseCaching.MAX_ITEMS:
            last = self.orderCache.pop()
            del self.cache_data[last]
            print('DISCARD: {}'.format(last))

        if key not in self.orderCache:
            self.orderCache.append(key)
        else:
            self.orderCache.remove(key)
            self.orderCache.append(key)

        def get(self, key):
            """ get method"""
            return self.cache_data.get(key)
