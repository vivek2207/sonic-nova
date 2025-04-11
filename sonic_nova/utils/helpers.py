"""Utility functions for the Sonic Nova application.

This module provides utility functions used throughout the application, including:
- Debug printing functionality
- Timing decorators for both synchronous and asynchronous functions
- Performance monitoring tools

The utilities in this module are designed to be reusable and help with:
- Debugging and troubleshooting
- Performance profiling
- Code instrumentation
"""

import time
import asyncio
import functools
from sonic_nova.config.settings import is_debug

def debug_print(message):
    """Print debug messages when debug mode is enabled.
    
    This function checks if debug mode is enabled before printing,
    ensuring debug messages only appear when needed.
    
    Args:
        message (str): The debug message to print
    
    Example:
        >>> debug_print("Processing audio chunk")
        [DEBUG] Processing audio chunk
    """
    if is_debug():
        print(f"[DEBUG] {message}")

def time_it(name, func=None):
    """Decorator to measure and log the execution time of a synchronous function.
    
    This decorator can be used with or without arguments. It will print the
    execution time of the decorated function if debug mode is enabled.
    
    Args:
        name (str): A descriptive name for the timed operation
        func (callable, optional): The function to decorate
    
    Returns:
        callable: The decorated function
    
    Example:
        >>> @time_it("process_data")
        ... def process_data():
        ...     time.sleep(1)
        >>> process_data()
        [DEBUG] process_data took 1.00 seconds
    """
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
    """Decorator to measure and log the execution time of an asynchronous function.
    
    Similar to time_it, but designed for async functions. It will print the
    execution time of the decorated async function if debug mode is enabled.
    
    Args:
        name (str): A descriptive name for the timed operation
        func (callable, optional): The async function to decorate
    
    Returns:
        callable: The decorated async function
    
    Example:
        >>> @time_it_async("async_process")
        ... async def process_data():
        ...     await asyncio.sleep(1)
        >>> await process_data()
        [DEBUG] async_process took 1.00 seconds
    """
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