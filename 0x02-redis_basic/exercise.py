#!/usr/bin/env python3
"""
This module provides a Cache class to interact with Redis,
allowing storage of various data types with randomly generated keys.
"""

import redis
import uuid
from typing import Union


class Cache:
    """
    Cache class to interface with Redis, storing data with
    a randomly generated keys.
    """
    def __init__(self):
        """
        Initializes the Cache instance by creating a Redis client
        and flushing the db.
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Stores the given data in Redis with a random UUID as the key.

        Args:
            data (str, bytes, int, float): The data to store in Redis.

        Returns:
            str: The generated key under which the data is stored.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
