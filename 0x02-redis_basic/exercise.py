#!/usr/bin/env python3
"""Redis introduction"""
import redis
import typing
import uuid


class Cache():
    """Cache class making use of redis"""
    def __init__(self):
        """Initializer for the Cache class"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: typing.Union[str, int, bytes, float]) -> str:
        """store method generates a string using uuid"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
    
    def get(self, key: str, fn: typing.Callable[[], str]=None) -> str:
        """Get method to return the dsired format of the input key"""
        try:
            if (fn == None):
                return self._redis.get(key)
            else:
                attr = self._redis.get(key)
                return fn(attr)
        except Exception as e:
            return None
        
    def get_str(self, key) -> str:
        """Returns a key if str is intended"""
        return str(key)
    
    def get_int(self, key) -> int:
        """Returna an int conversion"""
        return int(key)
