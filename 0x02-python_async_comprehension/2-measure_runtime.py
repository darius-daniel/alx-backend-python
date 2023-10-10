#!/usr/bin/env python3
"""2. Run time for four parallel comprehensions"""
import time
import asyncio
from typing import AsyncGenerator

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Executes async_comprehension four times in parallel using
    asyncio.gather(), and measures the total runtime and returns it.
    :return: the total runtime of executing async_comprehension four time in
    parallel
    """
    start: float = time.time()
    await asyncio.gather(
        *[async_comprehension() async for num in number(4)])
    end: float = time.time()

    return end - start


async def number(times: int) -> AsyncGenerator[int, None]:
    """
    Yields async_comprehension @times times
    :param times: number of times async_comprehension is yielded by the
        function
    :return: Nothing
    """
    for i in range(times):
        yield i
        await asyncio.sleep(1)
