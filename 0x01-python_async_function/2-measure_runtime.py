#!/usr/bin/env python3
"""2. Measure the runtime. """
import time
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total execution time for wait_n(n, max_delay), and returns
    total_time / n
    :param n: number of times wait_n will be executed
    :param max_delay: maximum delay time per execution
    :return: total execution time total_time / number of times wait_n is
        executed n
    """
    start: float = time.time()
    asyncio.run(wait_n(n, max_delay))
    end: float = time.time()

    return (end - start) / n
