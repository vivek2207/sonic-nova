"""Utility functions for the Sonic Nova application."""

import time
import asyncio
import functools
from sonic_nova.config.settings import is_debug

def debug_print(message):
    """Print debug messages if debug mode is enabled."""
    if is_debug():
        print(f"[DEBUG] {message}")

def time_it(name, func=None):
    """Decorator to measure and log the execution time of a function."""
    if func is None:
        return lambda f: time_it(name, f)
    
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        debug_print(f"{name} took {end_time - start_time:.2f} seconds")
        return result
    return wrapper

def time_it_async(name, func=None):
    """Decorator to measure and log the execution time of an async function."""
    if func is None:
        return lambda f: time_it_async(name, f)
    
    if not asyncio.iscoroutinefunction(func):
        return func
    
    @functools.wraps(func)
    async def wrapper(*args, **kwargs):
        start_time = time.time()
        result = await func(*args, **kwargs)
        end_time = time.time()
        debug_print(f"{name} took {end_time - start_time:.2f} seconds")
        return result
    return wrapper 