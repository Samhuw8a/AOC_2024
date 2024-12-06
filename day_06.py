from utils.all import *

input = read_input_line(6, sep="\n")
# input = read_input_line("test_06", sep="\n")
input = mapl(list, input)

G: dict = {}
start = (0, 0)

for i in range(len(input)):
    for j in range(len(input[0])):
        G[(i, j)] = input[i][j]
        if input[i][j] == "^":
            start = (i, j)


def invert_choords(c: tuple):
    if c == (1, 0):  # Down
        return (-1, 0)
    elif c == (-1, 0):  # Up
        return (1, 0)
    elif c == (0, -1):  # Left
        return (0, 1)
    elif c == (0, 1):  # Right
        return (0, -1)


def rotate_choords_90(c: tuple):
    if c == (1, 0):  # Down
        return (0, -1)
    elif c == (-1, 0):  # Up
        return (0, 1)
    elif c == (0, -1):  # Left
        return (-1, 0)
    elif c == (0, 1):  # Right
        return (1, 0)


def inc(c: tuple, v: tuple) -> tuple:
    return (c[0] + v[0], c[1] + v[1])


def is_on_line(c: tuple, location: tuple, vector: tuple) -> bool:
    if vector == (0, 1) or vector == (0, -1):
        return c[0] == location[0]
    if vector == (1, 0) or vector == (-1, 0):
        return c[1] == location[1]
    return False


def part_1() -> int:
    seen = set()
    chord = start
    vect = (-1, 0)
    while chord in G.keys():
        nxt = inc(chord, vect)
        if G.get(nxt, "") == "#":
            vect = rotate_choords_90(vect)
        else:
            seen.add(chord)
            chord = nxt

    return len(seen)


def sim_until_loop(grid: dict, start):
    seen = set()
    chord = start
    vect = (-1, 0)
    while chord in grid.keys():
        if (chord,vect) in seen:
            return True
        nxt = inc(chord, vect)
        if grid.get(nxt, "") == "#":
            vect = rotate_choords_90(vect)
        else:
            seen.add((chord,vect))
            chord = nxt

    return False


def part_2() -> int:
    seen: set = set()
    obst: set = set()
    chord = start
    vect = (-1, 0)
    while chord in G.keys():
        nxt = inc(chord, vect)
        if G.get(nxt, "") == "#":
            vect = rotate_choords_90(vect)
        else:
            g = G.copy()
            g[chord] = "#"
            if sim_until_loop(g, start):
                obst.add(chord)
            seen.add((chord, vect))
            chord = nxt

    # for c in input:
        # for char in c:
            # print(char, end="")
        # print()
    return len(obst)


print(part_1())
print(part_2())
