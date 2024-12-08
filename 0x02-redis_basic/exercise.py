#!/usr/bin/env python3
"""
Contains the class definition for redis cache
"""
import redis
import uuid
from functools import wraps
from typing import Union, Callable, Optional


def count_calls(method: Callable) -> Callable:
    """
    A decorator to count how many times a method has been called.
    It increments a Redis counter every time the method is invoked.
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        counter_key = method.__qualname__
        self._redis.incr(counter_key)
        result = method(self, *args, **kwargs)
        return result
    return wrapper


def call_history(method: Callable) -> Callable:
    """
    A decorator to store the inputs and outputs of a
    method in Redis lists.
    The inputs are stored in a list with ":inputs", and outputs in
    a list with ":outputs".
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        input_key = method.__qualname__ + ":inputs"
        output_key = method.__qualname__ + ":outputs"
        self._redis.rpush(input_key, str(args))
        result = method(self, *args, **kwargs)
        self._redis.rpush(output_key, str(result))
        return result
    return wrapper


def replay(method: Callable) -> None:
    """
    Replays the history of a function
    Args:
        method: The function to be decorated
    Returns:
        None
    """
    name = method.__qualname__
    cache = redis.Redis()
    calls = cache.get(name).decode("utf-8")
    print("{} was called {} times:".format(name, calls))
    inputs = cache.lrange(name + ":inputs", 0, -1)
    outputs = cache.lrange(name + ":outputs", 0, -1)
    for i, o in zip(inputs, outputs):
        print("{}(*{}) -> {}".format(name, i.decode('utf-8'),
                                     o.decode('utf-8')))


class Cache:
    def __init__(self):
        """Initialize the Cache class and flush the Redis instance."""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Generate a random key, store the data in Redis, and return the key.

        Args:
            data (Union[str, bytes, int, float]): The data to store.

        Returns:
            str: The key under which the data is stored.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self,
            key: str,
            fn: Optional[Callable[[bytes],
                                  Union[str, int,
                                  bytes]]] = None) -> Optional[Union[str,
                                                                     int,
                                                                     bytes]]:
        """
        Retrieve data from Redis by key, optionally converting it using fn.

        Args:
            key (str): The key to retrieve.
            fn (Callable[[bytes], Any], optional):
            A callable to convert the data.

        Returns:
            Optional[Union[str, int, bytes]]: The retrieved data,
            converted if fn is provided.
        """
        value = self._redis.get(key)
        if value is None:
            return None
        return fn(value) if fn else value

    def get_str(self, key: str) -> Optional[str]:
        """
        Retrieve data as a UTF-8 string.

        Args:
            key (str): The key to retrieve.

        Returns:
            Optional[str]: The retrieved data as a string.
        """
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> Optional[int]:
        """
        Retrieve data as an integer.

        Args:
            key (str): The key to retrieve.

        Returns:
            Optional[int]: The retrieved data as an integer.
        """
        return self.get(key, fn=int)

    def count(self, method_name: str) -> int:
        """
        Get the number of times a method has been called.

        Args:
            method_name (str): The name of the method to
            get the call count for.

        Returns:
            int: The number of times the method has been called.
        """
        counter_key = method_name + ":calls"
        return int(self._redis.get(counter_key) or 0)
