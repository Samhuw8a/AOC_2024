from utils.all import *
import numpy as np

input = read_input_line(4, sep="\n")
# input = read_input_line("test_04", sep="\n")
input_vert = transpose(list(input))
input_vert = mapl("".join, input_vert)
input_diag_hor: list = []
input_diag_ver: list = []

SEARCH: tuple = ("XMAS", "SAMX")

for i in range(len(input)):
    input_diag_hor.append(mapl(str, np.diagonal(mapl(list, input), offset=i)))

for i in range(1, len(input)):
    input_diag_hor.append(mapl(str, np.diagonal(mapl(list, input), offset=-i)))

for i in range(len(input_vert)):
    input_diag_ver.append(mapl(str, np.diagonal(mapl(list, input[::-1]), offset=i)))

for i in range(1, len(input_vert)):
    input_diag_ver.append(mapl(str, np.diagonal(mapl(list, input[::-1]), offset=-i)))

input_diag_hor = mapl("".join, input_diag_hor)
input_diag_ver = mapl("".join, input_diag_ver)


def part_1() -> int:
    tot = 0
    for line_hori in input:
        tot += line_hori.count(SEARCH[0])
        tot += line_hori.count(SEARCH[1])
    for line_vert in input_vert:
        tot += line_vert.count(SEARCH[0])
        tot += line_vert.count(SEARCH[1])
    for line_diag in input_diag_hor:
        tot += line_diag.count(SEARCH[0])
        tot += line_diag.count(SEARCH[1])
    for line_diagv in input_diag_ver:
        tot += line_diagv.count(SEARCH[0])
        tot += line_diagv.count(SEARCH[1])
    return tot


def ecken(x: int, y: int) -> tuple:
    return ((-1, -1), (-1, 1), (1, -1), (1, 1))


def part_2() -> int:
    tot = 0
    for i in range(1, len(input) - 1):
        for j in range(1, len(input[0]) - 1):
            if input[i][j] == "A":
                vals = mapl(lambda x: input[x[0]+i][x[1]+j], ecken(i, j))
                if vals.count("M")==2 and vals.count("S") ==2 and not vals[0]==vals[-1]:
                    tot +=1

    return tot


print(part_1())
print(part_2())
