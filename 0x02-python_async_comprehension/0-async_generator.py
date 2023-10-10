#!/usr/bin/env python3
"""0. Async Generator"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[int, None, None]:
    """
    Loops 10 times, each time asynchronously wait 1 second, and yields a
    random number between 0 and 10.
    :return:
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.randint(0, 10)
