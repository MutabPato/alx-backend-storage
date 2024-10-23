#!/usr/bin/env python3
"""Redis basic"""

import redis
import uuid


class Cache():
    def __init__(self):
        """Connect to Redis and clear the database"""
        self._redis = redis.Redis(host='localhost', port=6379, db=0)
        self._redis.flushdb()

    def store(self, data: any) -> str:
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
