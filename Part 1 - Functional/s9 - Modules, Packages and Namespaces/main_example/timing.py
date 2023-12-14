# timing.py
print("loading timing...")

"""
How long a snippet of code takes to run over multiple iterations
"""

from time import perf_counter
from collections import namedtuple
import argparse

Timing = namedtuple("Timing", "repeats elapsed average")


def timeit(code, repeats=10):
    code = compile(code, filename="<string>", mode="exec")
    start = perf_counter()
    for _ in range(repeats):
        exec(code)
    end = perf_counter()
    elapsed = end - start
    average = elapsed / repeats
    return Timing(repeats, elapsed, average)
