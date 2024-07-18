#!/usr/bin/env python3
"""Redis basic"""

import redis
import requests

client = redis.StrictRedis(host='localhost', port=6379, db=0)


def get_page(url: str) -> str:
    """obtain the HTML content of a particular URL and returns it"""
    # Generate cache key for the url
    cache_key = f"cache:{url}"
    count_key = f"count:{url}"

    # Increment the access count
    client.incr(count_key)

    # Check if the URL content is already cached
    cached_content = client.get(cache_key)
    if cached_content:
        print("Using cached data")
        return cached_content.decode('utf-8')

    # Fetch the HTML content from the URL
    response = requests.get(url)
    html_content = response.text

    # Cache the HTML content with an expiration of 10 sec
    client.setex(cache_key, 10, html_content)

    return html_content
