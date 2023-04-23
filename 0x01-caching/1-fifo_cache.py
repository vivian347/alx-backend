#!/usr/bin/env python3
"""FIFO cache"""

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """inherits from BaseCaching and is a caching system"""

    def __init__(self):
        """initialize"""
        super().__init__()
        self.key_list = []

    def put(self, key, item):
        """use FIFO algos to assign dict valsss"""
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            oldest_key = self.key_list.pop(0)
            del self.cache_data[oldest_key]
            print("DISCARD: ", oldest_key)
        if key is None or item is None:
            return
        self.cache_data[key] = item
        self.key_list.append(key)

    def get(self, key):
        """return val in dict linked to key"""
        if key in self.cache_data and key is not None:
            return self.cache_data[key]
        else:
            return None
