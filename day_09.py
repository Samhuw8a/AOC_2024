from utils.all import *
from collections import deque
from enum import Enum


class State(Enum):
    Empty = 0
    File = 1


rinput = read_input_line(9,sep="\n")[0]
# rinput = read_input_line("test_09", sep="\n")[0]
input = digits(rinput)


def get_all_files(nums: list) -> deque:
    stack: deque = deque([])
    id = 0
    for i in range(0, len(nums), 2):
        stack.extend(id for i in range(nums[i]))
        id += 1
    return stack


def get_all_files_ids(nums: list) -> list:
    stack: list = []
    id = 0
    for i in range(0, len(nums)):
        if i % 2 == 0:
            stack.append([nums[i], id, State.File, False])
            id += 1
        else:
            stack.append([nums[i], 0, State.Empty, False])
    return stack


def print_files(files: list) -> None:
    for i in files:
        if i[2] == State.Empty:
            print("." * i[0], end="")
        elif i[2] == State.File:
            print(str(i[1]) * i[0], end="")
    print()


def find_empty(nums: list, file_ind: int) -> list:
    size, id, typ, visited = nums[file_ind]
    for i in range(len(nums)):
        if i == file_ind:
            break
        if nums[i][0] >= size and nums[i][2] == State.Empty:
            nums[i][0] -= size
            nums[file_ind - 1][0] += size
            nums.insert(i, nums.pop(file_ind))
            break

    return nums


def checksum(nums: list) -> int:
    tot = 0
    for i in range(len(nums)):
        tot += i * nums[i]
    return tot


def checksum2(nums: list) -> int:
    tot = 0
    # nums = filterl(lambda x: x[2] == State.File, nums)
    files = []
    for el in nums:
        files.extend([el[1]] * el[0])
    # print(files)
    # print_files(nums)
    return checksum(files)


def part_1() -> int:
    index = 0
    new: list = []
    files = get_all_files(input)
    while files:
        if index % 2 == 0:
            for i in range(input[index]):
                x = files.popleft()
                new.append(x)
                if not files:
                    break
        else:
            for i in range(input[index]):
                x = files.pop()
                new.append(x)
                if not files:
                    break
        index += 1
        # print(files)
    # print(new)
    return checksum(new)


def part_2() -> int:
    new: list = []
    files = get_all_files_ids(input)
    for obj in autorange(len(files) - 1, 0):
        # print_files(files)
        if files[obj][2] == State.Empty:
            continue
        else:
            files = find_empty(files, obj)

    return checksum2(files)


print(part_1())
print(part_2())
