#!/usr/bin/env python3
"""1. Async Comprehensions"""
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[int]:
    """
     Collects 10 random numbers using an async comprehension over
     async_generator, then return the 10 random numbers.
    :return: list of 10 randomly generated numbers
    """
    return [i async for i in async_generator()]
