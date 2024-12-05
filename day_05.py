from utils.all import *
from collections import defaultdict
from typing import Any

input = read_input_line(5, sep="\n\n")
# input = read_input_line("test_05", sep="\n\n")

arules, aupdates = input
rules: list = arules.split("\n")
rule: defaultdict = defaultdict(list)
for i in rules:
    x, y = i.split("|")
    rule[y].append(x)
updates: list = mapl(integers, aupdates.split("\n"))


def middle(m: list) -> Any:
    middle = len(m) // 2
    return m[middle]


def correct(update: list) -> bool:
    in_order: bool = True
    for i in range(len(update)):
        after = update[i + 1:]
        for j in rule[str(update[i])]:
            if int(j) in after:
                in_order = False
    return in_order


def part_1() -> int:
    tot = 0
    for update in updates:
        if correct(update):
            tot += middle(update)
    return tot


def change(update: list) -> list:
    for i in range(len(update)):
        after = update[i + 1:]
        for j in rule[str(update[i])]:
            if int(j) in after:
                update.remove(int(j))
                update.insert(i, int(j))
    if not correct(update):
        update = change(update)

    return update


def part_2() -> int:
    incorrect = list(filter(lambda x: not correct(x), updates))
    changed = list(map(change, incorrect))
    middles = map(middle, changed)
    return sum(middles)


print(part_1())
print(part_2())
