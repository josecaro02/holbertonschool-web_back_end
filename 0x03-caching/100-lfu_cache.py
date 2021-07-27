#!/usr/bin/env python3
""" lfu cache task"""

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """ LFU caching"""

    def __init__(self):
        """ overload init"""
        super().__init__()
        self.orderCache = []
        self.count = {}

    def put(self, key, item):
        """ put method"""
        if key is None or item is None:
            return

        self.cache_data[key] = item
        item_count = self.count.get(key)

        if item_count is not None:
            self.count[key] += 1
        else:
            self.count[key] = 1

        if len(self.cache_data.keys()) > BaseCaching.MAX_ITEMS:
            del self.cache_data[self.orderCache[0]]
            del self.count[self.orderCache[0]]
            print("DISCARD: {}".format(self.orderCache[0]))
            self.orderCache.pop(0)

        if key not in self.orderCache:
            self.orderCache.insert(0, key)
        self.moveRight(key)

    def get(self, key):
        """ get method"""
        item = self.cache_data.get(key)
        if item is not None:
            self.count[key] += 1
            self.moveRight(key)
        return item

    def moveRight(self, key):
        """ move right list method"""
        lenCache = len(self.orderCache)
        idx = self.orderCache.index(key)
        item_count = self.count[key]

        for i in range(idx, lenCache):
            if i != (lenCache - 1):
                nextItem = self.orderCache[i + 1]
                nextCount = self.count[nextItem]

                if nextCount > item_count:
                    break

        self.orderCache.insert(i + 1, key)
        self.orderCache.remove(key)
