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

def call_history(method: Callable) -> Callable:
    """store the history of inputs and outputs for a particular function"""
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        # preparing keys for inputs and outputs
        inputs_key = f"{method.__qualname__}:inputs"
        outputs_key = f"{method.__qualname__}:outputs"
        
        # convert args to string for storage
        args_str = str(args)

        # record inputs
        self._redis.rpush(inputs_key, args_str)

        # call original method
        result = method(self, *args, **kwargs)

        # record outputs
        self._redis.rpush(outputs_key, str(result))

        return result
    return wrapper

class Cache:
    """Cache class"""
    def __init__(self):
        """store an instance of the Redis client as a private variable
        and flush the instance"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
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

    def replay(method: Callable):
        # preparing keys for inputs and outputs
        inputs_key = f"{method.__qualname__}:inputs"
        outputs_key = f"{method.__qualname__}:outputs"
        
        # connect to redis
        r = redis.Redis()

        # Retrieve input and outputs from redis
        inputs = r.lrange(inputs_key, 0, -1)
        outputs = r.lrange(outputs_key, 0, -1)

        print(f"{method.__qualname__} was called {len(inputs)} times:")

        for input, output in zip(inputs, outputs):
            print(f"{method.__qualname__}(*{input.decode('utf-8')}) -> {output.decode('utf-8')}")
