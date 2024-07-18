#!/usr/bin/env python3
"""Redis basic"""

import redis
import uuid
import requests
from typing import Union, Callable
from functools import wraps


r = redis.Redis()


def cache_page(method: Callable) -> Callable:
    """Decorator to track how many times a particular URL was accessed
    and cache the result with an expiration time of 10 seconds"""
    def decorator(func):
        @wraps(func)
        def wrapper(url, *args, **kwargs):
            """wrapper method"""
            r.incr(f"count:{url}")

            cached_result = r.get(url)
            if cached_result:
                print("Using cached data")
                return cached_result.decode('utf-8')

            result = func(url, *args, **kwargs)
            r.set(url, result, ex=expire_time)
            return result
        return wrapper
    return decorator


@cache_page
def get_page(url: str) -> str:
    """uses the requests module to obtain the HTML content
    of a particular URL and returns it"""

    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(f"An error has occurred: {e}")
        return ""
