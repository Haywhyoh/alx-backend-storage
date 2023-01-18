#!/usr/bin/env python3
""" Random task assigned by alx"""
import redis
import uuid
from typing import Union, Optional, Callable
from functools import wraps

def count_calls(method: Callable) -> Callable:
    """ to count how many times methods of the Cache class are called """
    key = method.__qualname__

    @wraps(method)
    def wrapper_function(self, *args, **kwargs):
        """ wrapped function """
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper_function


class Cache():
    """Cache class. for some redis method"""
    def __init__(self):
        """the __init__ method,
          store an instance of the Redis client as a private variable
          named _redis (using redis.Redis()) and flush the
          instance using flushdb"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """store method that takes a data argument and returns a string.
        The method should generate a random key (e.g. using uuid), store
        the input data in Redis using the random key
        and return the key."""
        id = str(uuid.uuid4())
        self._redis.set(id, data)
        return id

    def get(self, key, fn: Optional[Callable]) -> Union[int,
                                                        bytes, str, float]:
        """ take a key string argument and an optional Callable argument named
            fn. This callable will be used to convert the data back to the
            desired format """
        data = self._redis.get(key)
        if fn:
            return fn(data)
        return data

    def get_str(self, key):
        """ automatically parametrize Cache.get to str """
        data = self._redis.get(key).decode('utf-8')
        return data

    def get_int(self, key):
        """ automatically parametrize Cache.get to int """
        data = self._redis.get(key)
        try:
            data = int(data.decode("utf-8"))
        except Exception:
            data = 0
        return data
