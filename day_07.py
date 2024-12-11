from utils.all import *
from itertools import product, chain
from more_itertools import interleave_longest

rinput = read_input_line(7,sep="\n")
# rinput = read_input_line("test_07", sep="\n")
input: list = [(int(i.split(":")[0]), integers(i.split(":")[1]))for i in rinput]


def solve(result: int, nums: list) -> bool:
    if result == 0 and len(nums) == 0:
        return True
    elif result < 0 or len(nums) == 0:
        return False

    # num = nums.pop()
    num = nums[-1]
    nums = nums[:-1]
    if result % num == 0:
        return solve(result // num, nums) or solve(result - num, nums)

    return solve(result - num, nums)


def solve2(result: int, nums: list) -> bool:
    if result == 0 and len(nums) == 0:
        return True
    elif result < 0 or len(nums) == 0:
        return False

    # num = nums.pop()
    num = nums[-1]
    nums = nums[:-1]
    two = False
    con = False
    if result % num == 0:
        two = solve2(result // num, nums)
    if str(result).endswith(str(num)) and len(str(result)) > len(str(num)):
        nres = int(str(result)[:-len(str(num))])
        con = solve2(nres, nums)

    return con or two or solve2(result - num, nums)


def part_1() -> int:
    tot = 0
    for res, nums in input:
        if solve(res, nums):
            tot += res
    return tot


def part_2() -> int:
    tot = 0
    for res, nums in input:
        if solve2(res, nums):
            # print(res)
            tot += res
    return tot


print(part_1())
print(part_2())
