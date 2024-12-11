from utils.all import *
from collections import defaultdict
from itertools import combinations

input = read_input_line(8,sep="\n")
# input = read_input_line("test_08", sep="\n")
input = mapl(list, input)
G: dict = {}
NODES: defaultdict = defaultdict(list)

for i in range(len(input)):
    for j in range(len(input[0])):
        G[(i, j)] = input[i][j]
        if input[i][j] != ".":
            NODES[input[i][j]].append((i, j))


def inc(c: tuple, v: tuple) -> tuple:
    return (c[0] + v[0], c[1] + v[1])


def mul(c: tuple, v: tuple) -> tuple:
    return (c[0] * v[0], c[1] * v[1])


def dist(c: tuple, v: tuple) -> tuple:
    return (c[0] - v[0], c[1] - v[1])


def part_1() -> int:
    anti: set = set()
    for node in NODES.keys():
        for pair in combinations(NODES[node], 2):
            n1 = inc(pair[0], dist(pair[0], pair[1]))
            n2 = inc(pair[1], dist(pair[1], pair[0]))
            if n1 in G.keys():
                input[n1[0]][n1[1]] = "#"
                anti.add(n1)
            if n2 in G.keys():
                input[n2[0]][n2[1]] = "#"
                anti.add(n2)
    # for i in input:
        # for c in i:
            # print(c,end ="")
        # print()

    return len(anti)


def part_2() -> int:
    anti: set = set()
    for node in NODES.keys():
        for pair in combinations(NODES[node], 2):
            anti.add(pair[0])
            anti.add(pair[1])
            n1 = inc(pair[0], dist(pair[0], pair[1]))
            n2 = inc(pair[1], dist(pair[1], pair[0]))
            while n1 in G.keys():
                anti.add(n1)
                input[n1[0]][n1[1]] = "#"
                n1 = inc(n1, dist(pair[0], pair[1]))
            while n2 in G.keys():
                anti.add(n2)
                input[n2[0]][n2[1]] = "#"
                n2 = inc(n2, dist(pair[1], pair[0]))
    for i in input:
        for c in i:
            print(c, end="")
        print()

    return len(anti)


print(part_1())
print(part_2())
