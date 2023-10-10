#!/usr/bin/env python3
"""2. Run time for four parallel comprehensions"""
import time
import asyncio
from typing import Callable, Generator, List

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
        *[func() async for func in call_async_comprehension(4)])
    end: float = time.time()

    return end - start


async def call_async_comprehension(
        times: int) -> Generator[Callable[[], List[int]], None, None]:
    """
    Yields async_comprehension @times times
    :param times: number of times async_comprehension is yielded by the
        function
    :return: Nothing
    """
    for i in range(times):
        await asyncio.sleep(1)
        yield async_comprehension
