#!/usr/bin/env python3
"""Mru cache task"""

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """class Mru cache"""

    def __init__(self):
        """ overload init"""
        super().__init__()
        self.orderCache = []

    def put(self, key, item):
        """put method"""
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
        item = self.cache_data.get(key)
        if item is not None:
            self.orderCache.remove(key)
            self.orderCache.append(key)
        return item
