from utils.all import *
from typing import Iterable
from functools import lru_cache
import math

rinput = read_input_line(11, sep="\n")[0]
# rinput = read_input_line("test_11", sep="\n")[0]

input = list(integers(rinput))


@lru_cache(None)
def rules(stone: int) -> tuple:
    if stone == 0:
        return (1,)
    else:
        length = int(math.log10(stone)) + 1
        if length % 2 == 0:
            length = length // 2
            length = int(math.pow(10, length))
            return (int(stone // length), int(stone % length))

        else:
            return (stone * 2024,)


@lru_cache(None)
def calculate(stone: int, n: int = 75) -> int:
    if n == 0:
        return 1

    elif stone == 0:
        return calculate(1, n - 1)

    length = int(math.log10(stone)) + 1
    if length % 2 == 0:
        length = length // 2
        length = int(math.pow(10, length))
        return calculate(int(stone // length), n - 1) + calculate(int(stone % length), n - 1)

    return calculate(stone * 2024, n - 1)


def blink(stones: list) -> list:
    new: list = []
    for stone in stones:
        new.extend(rules(stone))
    return new


def part_1() -> int:
    stones = input.copy()
    for _ in range(25):
        stones = blink(stones)
    return len(stones)


def part_2() -> int:
    stones = input.copy()
    return sum(map(calculate, stones))


print(part_1())
print(part_2())
