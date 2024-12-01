from utils.helpers import *
from collections import Counter

input_1 = read_input_line(1, sep="\n")
# input_1 = read_input_line("test_01", sep="\n")

l1: list = []
l2: list = []
for i in input_1:
    line = list(integers(i))
    l1.append(line[0])
    l2.append(line[1])
l1.sort()
l2.sort()


def part_1() -> int:
    tot: int = 0
    for i, j in zip(l1, l2):
        tot += abs(i-j)
    return tot


def part_2() -> int:
    c2 = Counter(l2)
    tot: int = 0
    for i in l1:
        tot += i*c2[i]  # type:ignore
    return tot


print(part_1())
print(part_2())
