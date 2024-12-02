from utils.all import *

input = read_input(2, sep="\n")
# input = read_input("test_02", sep="\n")
input = mapl(integers, input[:-1])


def f(vals: list) -> list:
    delta: list = []
    for i in range(len(vals)-1):
        delta.append(vals[i]-vals[i+1])
    return delta


def part_1(vals: list) -> bool:
    deltas = f(vals)
    if max(map(abs, deltas)) > 3:
        return False
    elif min(deltas) == 0:
        return False
    if not len(set(mapl(sign, deltas))) == 1:
        return False
    return True


def part_2(vals: list) -> bool:
    deltas = f(vals)
    absdeltas = map(abs, deltas)
    if max(absdeltas) > 3 or min(deltas) == 0 or not len(set(mapl(sign, deltas))) ==1:
        for i in range(len(vals)):
            new_vals = list(vals)
            new_vals.pop(i)
            if part_1(new_vals):
                return True
        return False
    return True


# print(input)
print(sum(mapl(part_1, input)))
print(sum(mapl(part_2, input)))
