#!/usr/bin/env python3
"""Basic cache"""

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """inherits from BaseCaching and is a caching system"""

    def put(self, key, item):
        """assign to the dict the item val for key"""
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """return val in dict linked to key"""
        if key in self.cache_data and key is not None:
            return self.cache_data[key]
        else:
            return None
