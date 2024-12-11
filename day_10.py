from utils.all import *
from collections import deque

input = read_input_line(10, sep="\n")
# input = read_input_line("test_10", sep="\n")

G: dict = {}
start: list = []
for i in range(len(input)):
    for j in range(len(input[0])):
        G[(i, j)] = int(input[i][j])
        if input[i][j] == "0":
            start.append((i, j))


def get_neighbors(chord: tuple, graph: dict) -> tuple:
    neighbor = ((chord[0] + 1, chord[1]), (chord[0], chord[1] + 1),
                (chord[0] - 1, chord[1]), (chord[0], chord[1] - 1))
    return tuple(filter(lambda x: graph.get(x) == graph.get(chord, 0) + 1, neighbor))


def search(start: tuple, graph: dict) -> int:
    queue: deque = deque([start])
    visited: set = set()

    heads = 0
    while queue:
        node = queue.pop()
        if node in visited:
            continue
        if G.get(node) == 9:
            heads += 1
            visited.add(node)
            continue

        visited.add(node)
        queue.extend(get_neighbors(node, G))

    return heads


def search_trails(start: tuple, graph: dict) -> int:
    queue: deque = deque([(start, [])])

    trails: list = []
    while queue:
        node, trail = queue.popleft()
        if (node, trail) in trail:
            continue
        if G.get(node) == 9:
            trails.append(tuple(trail))
            continue

        trail.append((node, trail))
        queue.extend(map(lambda x: (x, trail.copy()), get_neighbors(node, G)))

    return len(trails)


def part_1() -> int:
    tot = 0
    for s in start:
        tot += search(s, G)
    return tot


def part_2() -> int:
    tot = 0
    for s in start:
        tot += search_trails(s, G)
    return tot


print(part_1())
print(part_2())
