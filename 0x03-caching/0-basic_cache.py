#!/usr/bin/env python3
""" basic cache task"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ BasicCache class"""

    def put(self, key, item):
        """Put method to base caching"""
        if item is not None and key is not None:
            self.cache_data[key] = item

    def get(self, key):
        """Get metho to base caching"""
        return self.cache_data.get(key)
