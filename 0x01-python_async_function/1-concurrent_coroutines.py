#!/usr/bin/env python3
"""
1. Execute multiple coroutines at the same time with async
"""

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> list[float]:
    """

    :param n:
    :param max_delay:
    :return:
    """
    import asyncio

    delays: list[float] = []

    for i in range(n):
        delays.append(await wait_random(max_delay))

    return delays
