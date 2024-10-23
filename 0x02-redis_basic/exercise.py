#!/usr/bin/env python3
"""Redis basic"""

import redis
import uuid
from typing import Union, Callable


class Cache():
    """Cache class
    """
    def __init__(self) -> None:
        """Connect to Redis and clear the database"""
        self._redis = redis.Redis(host='localhost', port=6379, db=0)
        self._redis.flushdb(True)

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Stores a value in a Redis data storage and returns the key"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Callable = None) -> Union[
            str, bytes, int, float]:
        """convert the data back to the desired format"""
        value = self._redis.get(key)
        if fn:
            return fn(value)
        return value

    def get_str(self, key: str) -> str:
        """Helper method to get the value as a string"""
        return self.get(key, lambda x: x.decode('utf-8') if x else None)

    def get_int(self, key: str) -> int:
        """Helper method to get the value as an integer"""
        return self.get(key, lambda x: int(x) if x else None)
