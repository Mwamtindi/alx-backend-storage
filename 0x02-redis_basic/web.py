#!/usr/bin/env python3
"""
This module provides a get_page function to retrieve HTML content from a URL,
track the number of accesses, and cache the result with an expiration time.
"""
import redis
import requests
exp = redis.Redis()
count = 0


def get_page(url: str) -> str:
    """Retrieves HTML content of a particular URL, caches it,
    and tracks access count."""
    exp.set(f"cached:{url}", count)
    res = requests.get(url)
    exp.incr(f"count:{url}")
    exp.setex(f"cached:{url}", 10, exp.get(f"cached:{url}"))
    return res.text

if __name__ == "__main__":
    get_page('http://slowwly.robertomurray.co.uk')
