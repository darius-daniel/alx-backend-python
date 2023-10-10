#!/usr/bin/env python3
"""2. Run time for four parallel comprehensions"""
import time
import asyncio

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Executes async_comprehension four times in parallel using
    asyncio.gather(), and measures the total runtime and returns it.
    :return: the total runtime of executing async_comprehension four time in
    parallel
    """
    start: float = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end: float = time.time()

    return end - start
