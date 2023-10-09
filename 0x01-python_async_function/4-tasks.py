#!/usr/bin/env python3
"""4. Tasks"""
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns wait_random n times with the specified max_delay
    :param n: number of times wait_random() is spawned
    :param max_delay: the maximum sleep length of asyncio.sleep()
    :return: a list of floats
    """
    delays: List[float] = []

    for i in range(n):
        delay: float = await task_wait_random(max_delay)

        i: int = 0
        while i < len(delays):
            if delays[i] >= delay:
                break
            i += 1

        delays.insert(i, delay)

    return delays
