#!/usr/bin/env python3
"""LIFO cache"""

BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """inherits from BaseCaching and is a caching system"""

    def __init__(self):
        """initialize"""
        super().__init__()

    def put(self, key, item):
        """use FIFO algos to assign dict valsss"""
        if key and item:
            self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            self.cache_data.pop(self.newest_item)
            print("DISCARD: ", self.newest_item)

        if key:
            self.newest_item = key

    def get(self, key):
        """return val in dict linked to key"""
        if key in self.cache_data and key is not None:
            return self.cache_data[key]
        else:
            return None
