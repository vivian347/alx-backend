#!/usr/bin/env python3
"""MRU cache"""

from collections import OrderedDict


BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """inherits from BaseCaching and is a caching system"""

    def __init__(self):
        """initialize"""
        super().__init__()
        self.cache_data = OrderedDict()
        self.mru = ""

    def put(self, key, item):
        """use MRU algos to assign dict valsss"""
        if key and item:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                if key in self.cache_data:
                    self.cache_data.update({key: item})
                    self.mru = key
                else:
                    discarded = self.mru
                    del self.cache_data[discarded]
                    print("DISCARD: {}".format(discarded))
                    self.cache_data[key] = item
                    self.mru = key

            else:
                self.cache_data[key] = item
                self.mru = key

    def get(self, key):
        """return val in dict linked to key"""
        if key in self.cache_data and key is not None:
            self.mru = key
            return self.cache_data[key]
        else:
            return None
