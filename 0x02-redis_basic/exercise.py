#!/usr/bin/env python3
"""Redis basic"""

import redis
import uuid
from typing import Union


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
