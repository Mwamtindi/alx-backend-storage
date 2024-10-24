#!/usr/bin/env python3
"""
This module provides get_page func to retrieve HTML content from a URL,
track the num of accesses, and cache result with expiration time.
"""

import requests
import redis
from typing import Callable
from functools import wraps

# Initialize Redis client
cache = redis.Redis()


def count_access(fn: Callable) -> Callable:
    """
    Decorator to count how many times URL was accessed and cache the result.
    """
    @wraps(fn)
    def wrapper(url: str) -> str:
        # Increment the access count for the URL
        cache_key_count = f"count:{url}"
        cache.incr(cache_key_count)

        # Check if the cached content exists
        cache_key_content = f"content:{url}"
        cached_content = cache.get(cache_key_content)

        if cached_content:
            # Return cached content if available
            return cached_content.decode('utf-8')

        content = fn(url)

        cache.setex(cache_key_content, 10, content)

        return content

    return wrapper


@count_access
def get_page(url: str) -> str:
    """
    Retrieves HTML content of URL, caches it, and tracks access count.

    Args:
        url (str): The URL to retrieve the HTML content from.

    Returns:
        str: The HTML content of the page.
    """
    response = requests.get(url)
    return response.text
