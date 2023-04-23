#!/usr/bin/env python3
"""LRU cache"""

from collections import OrderedDict


BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """inherits from BaseCaching and is a caching system"""

    def __init__(self):
        """initialize"""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """use LRU algos to assign dict valsss"""
        if key and item:
            self.cache_data[key] = item
            self.cache_data.move_to_end(key)

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            discarded = self.cache_data.popitem(last=False)

            print("DISCARD: {}".format(discarded[0]))

    def get(self, key):
        """return val in dict linked to key"""
        if key in self.cache_data and key is not None:
            self.cache_data.move_to_end(key)
            return self.cache_data[key]
        else:
            return None
