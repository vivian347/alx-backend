#!/usr/bin/env python3
"""FIFO cache"""

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """inherits from BaseCaching and is a caching system"""

    def __init__(self):
        """initialize"""
        super().__init__()

    def put(self, key, item):
        """use FIFO algos to assign dict valsss"""
        if key and item:
            self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            oldest_key = sorted(self.cache_data)[0]
            del self.cache_data[oldest_key]
            print("DISCARD: ", oldest_key)

        self.key_list.append(key)

    def get(self, key):
        """return val in dict linked to key"""
        return self.cache_data[key]
