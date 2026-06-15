#!/usr/bin/env python3
"""Module for measuring runtime of parallel comprehensions"""
import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Measure total runtime of 4 parallel async comprehensions"""
    start = time.time()
    await asyncio.gather(*[async_comprehension() for _ in range(4)])
    return time.time() - start
