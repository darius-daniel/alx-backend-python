#!/usr/bin/env python3
""""""
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Future:
    """
    Takes an integer max_delay and returns a asyncio.Task.
    :param max_delay: maximum function delay time
    :return: an asyncio.Task object
    """
    return asyncio.create_task(wait_random(max_delay))
