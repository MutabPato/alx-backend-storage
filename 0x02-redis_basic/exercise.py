#!/usr/bin/env python3
"""Redis basic"""
  
import redis
import uuid
from typing import Union, Callable
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """Decorator to count the number of calss to a method"""
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        self._redis.incr(method.__qualname__)
        return method(self, *args, **kwargs)
    return wrapper


class Cache:
    """Cache class"""
    def __init__(self):
        """store an instance of the Redis client as a private variable
        and flush the instance"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """generate a random key,
        store the input data in Redis using the random key
        and return the key"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Callable = None) -> Union[str, bytes, int, float]:
        data = self._redis.get(key)
        if data is None:
            return None
        if fn:
            return fn(data)
        return data

    def get_str(self, key: str) -> Union[str, None]:
        """parametrize Cache.get with str"""
        return(get(key, lambda d: d.decode("utf-8") if d else None))

    def get_int(self, key: str) -> Union[int, None]:
        """parametrize Cache.get with int"""
        return(get(key, lambda d: int(d) if d else None))

    @count_calls
    def incr(self, key: str) -> str:
        """Increments the count for the key every time the method is called"""
        return self._redis.incr(key)
