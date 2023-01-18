#!/usr/bin/env python3
""" Random task assigned by alx"""
import redis
import uuid
from typing import Union


class Cache():
    """Cache class. for some redis method"""
    def __init__(self):
        """the __init__ method,
          store an instance of the Redis client as a private variable
          named _redis (using redis.Redis()) and flush the
          instance using flushdb"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """store method that takes a data argument and returns a string.
        The method should generate a random key (e.g. using uuid), store
        the input data in Redis using the random key
        and return the key."""
        id = str(uuid.uuid4())
        self._redis.set(id, data)
        return id
