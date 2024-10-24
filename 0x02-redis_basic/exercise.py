#!/usr/bin/env python3
"""
This module provides a Cache class to interact with Redis,
allowing storage of various data types with randomly generated keys.
"""

import redis
import uuid
from typing import Union, Callable, Optional


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

    def get(self, key: str, fn: Optional[Callable] = None) -> Union[str, bytes, int, float, None]:
        """
        Retrieves the data stored at the given key,
        optionally applying a conversion func.

        Args:
            key (str): The key of the data to retrieve.
            fn (Callable, optional): A func to convert the
            retrieved data. Defaults to None.

        Returns:
            The data in Redis, with conversion applied if fn is provided.
        """
        data = self._redis.get(key)
        if data is None:
            return None
        if fn:
            return fn(data)
        return data

    def get_str(self, key: str) -> Optional[str]:
        """
        Retrieves data stored at given key and converts it to a UTF-8 string.

        Args:
            key (str): The key of the data to retrieve.

        Returns:
            str: The data as a UTF-8 string, or None if the key does not exist.
        """
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> Optional[int]:
        """
        Retrieves the data stored at the given key and converts it to integer.

        Args:
            key (str): The key of the data to retrieve.

        Returns:
            int: The data as an integer, or None if the key does not exist.
        """
        return self.get(key, fn=int)
