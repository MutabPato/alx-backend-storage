#!/usr/bin/env python3
"""Redis basic"""

import redis
import uuid
from typing import Union, Callable
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """Decorator to count the number of calls to a method"""
    key = method.__qualname__
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """Wrapper function to count method calls and execute the method"""
        self._redis.incr(key)
        return method(self, *args, **kwargs)

    return wrapper


def call_history(method: Callable) -> Callable:
    """Decorator to store the history of inputs and outputs
    for a particular function"""
    key = method.__qualname__
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """Wrapper function to store the history of inputs and outputs"""
        input_key = f"{key}:inputs"
        self._redis.rpush(input_key, str(args))

        result = method(self, *args, **kwargs)

        output_key = f"{key}:outputs"
        self._redis.rpush(output_key, str(result))

        return result

    return wrapper


class Cache():
    """Cache class
    """
    def __init__(self) -> None:
        """Connect to Redis and clear the database"""
        self._redis = redis.Redis(host='localhost', port=6379, db=0)
        self._redis.flushdb(True)

    @count_calls
    @call_history
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
