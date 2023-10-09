#!/usr/bin/env python3
"""
1. Execute multiple coroutines at the same time with async
"""
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> list[float]:
    """
    Spawns wait_random n times with the specified max_delay
    :param n: number of times wait_random() is spawned
    :param max_delay: the maximum sleep length of asyncio.sleep()
    :return: a list of floats
    """
    delays: list[float] = []

    for i in range(n):
        delay: float = await wait_random(max_delay)

        i: int = 0
        while i < len(delays):
            if delays[i] >= delay:
                break
            i += 1

        delays.insert(i, delay)

    return delays
