#!/usr/bin/env python3
"""
Fetch and cache web pages with request tracking.
"""
import redis
import requests
from functools import wraps
from typing import Callable

redis_client = redis.Redis()


def track_and_cache(ttl: int = 10) -> Callable:
    """
    Decorator to track how many times a URL is accessed
    and cache the HTML result for a specified time-to-live (TTL).
    """
    def decorator(method: Callable) -> Callable:
        @wraps(method)
        def wrapper(url: str) -> str:
            count_key = f"count:{url}"
            cache_key = f"cache:{url}"
            redis_client.incr(count_key)
            cached_response = redis_client.get(cache_key)
            if cached_response:
                return cached_response.decode("utf-8")
            response = method(url)
            redis_client.setex(cache_key, ttl, response)
            return response
        return wrapper
    return decorator


@track_and_cache(ttl=10)
def get_page(url: str) -> str:
    """
    Fetch the HTML content of a URL and return it.

    Args:
        url (str): The URL to fetch.

    Returns:
        str: The HTML content of the URL.
    """
    response = requests.get(url)
    return response.text
