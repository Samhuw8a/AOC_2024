from utils.helpers import *
import re

# input = read_input_line(3, sep="ökasjdföalskdhg")
input = read_input_line("test_03", sep="adsflkjasdfölkjasd")

pattern1 = re.compile(r"mul\([0-9]{1,3},[0-9]{1,3}\)")
pattern2 = re.compile(r"mul\([0-9]{1,3},[0-9]{1,3}\)|don't\(\)|do\(\)")


def part_1() -> int:
    tot = 0
    found = pattern1.findall(input[0])
    for el in found:
        nums = list(integers(el))
        tot += nums[0]*nums[1]
    return tot


def part_2() -> int:
    found = pattern2.findall(input[0])
    tot = 0
    enabled = True
    for el in found:
        if el == "do()":
            enabled = True
        elif el == "don't()":
            enabled = False
        elif enabled:
            nums = list(integers(el))
            tot += nums[0]*nums[1]
    return tot


print(part_1())
print(part_2())
