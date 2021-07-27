#!/usr/bin/env python3
"""lru cache task"""

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """class lru cache"""

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
            del self.cache_data[self.orderCache[0]]
            print('DISCARD: {}'.format(self.orderCache[0]))
            self.orderCache.pop(0)

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
