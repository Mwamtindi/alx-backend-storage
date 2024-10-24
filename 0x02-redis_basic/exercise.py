#!/usr/bin/env python3
"""
This module provides a Cache class to interact with Redis,allowing
storage of various data types with randomly generated keys.
"""
from typing import Union, Callable, Optional
from functools import wraps
import redis
import uuid


def call_history(method: Callable) -> Callable:
    """Stores history of inputs and outputs for a particular function"""
    methd_key = method.__qualname__
    inputs, outputs = methd_key + ':inputs', methd_key + ':outputs'

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        self._redis.rpush(inputs, str(args))
        result = method(self, *args, **kwargs)
        self._redis.rpush(outputs, str(result))
        return result
    return wrapper


def count_calls(method: Callable) -> Callable:
    """Creates and returns func that increments the count for tha
    key every time the method is called """
    methd_key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        self._redis.incr(methd_key)
        return method(self, *args, **kwargs)
    return wrapper


def replay(method: Callable) -> None:
    """Displays history of calls of a particular function"""
    methd_key = method.__qualname__
    inputs, outputs = methd_key + ':inputs', methd_key + ':outputs'
    redis = method.__self__._redis
    method_count = redis.get(methd_key).decode('utf-8')
    print(f'{methd_key} was called {method_count} times:')
    IOTuple = zip(redis.lrange(inputs, 0, -1), redis.lrange(outputs, 0, -1))
    for inp, outp in list(IOTuple):
        attr, data = inp.decode("utf-8"), outp.decode("utf-8")
        print(f'{methd_key}(*{attr}) -> {data}')


class Cache:
    """The cache class to handle redis operations."""
    def __init__(self):
        """stores the instance of the Redis client."""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Takes and stores data argument and returns a string."""
        key = str(uuid.uuid4())
        self._redis.mset({key: data})
        return key

    def get(self,
            key: str, fn: Optional[Callable] = None) -> str:
        """Takes a key string argument and an optional.
        Callable argument named fn."""
        data = self._redis.get(key)
        return fn(data) if fn is not None else data

    def get_str(self, data: str) -> str:
        """Returns the string value of decoded byte """
        return data.decode('utf-8', 'strict')

    def get_int(self, data: str) -> int:
        """Returns the integer value of decoded byte """
        return int(data)
