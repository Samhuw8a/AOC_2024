from utils.all import *
from collections import deque, defaultdict

input = read_input_line(12, sep="\n")
# input = read_input_line("test_12", sep="\n")


def edges(chord: tuple, graph: dict) -> int:
    x, y = chord
    node = graph[chord]
    tot = 0
    if graph.get((x + 1, y)) != node:
        tot += 1

    if graph.get((x, y + 1)) != node:
        tot += 1

    if graph.get((x - 1, y)) != node:
        tot += 1

    if graph.get((x, y - 1)) != node:
        tot += 1

    return tot


rawG: dict = {}
start: list = []
for i in range(len(input)):
    for j in range(len(input[0])):
        rawG[(i, j)] = input[i][j]


G: dict = {}
for el in rawG.keys():
    G[el] = [rawG[el], edges(el, rawG)]

VISITED: set = set()


def get_neighbors(chord: tuple, graph: dict) -> tuple:
    neighbor = ((chord[0] + 1, chord[1]), (chord[0], chord[1] + 1),
                (chord[0] - 1, chord[1]), (chord[0], chord[1] - 1))
    return tuple(filter(lambda x: graph.get(x, False), neighbor))


def size(start: tuple, typ: str) -> int:
    global VISITED
    queue: deque = deque([start])
    visited: set = set()
    edges = 0

    while queue:
        node = queue.pop()
        if node in visited:
            continue
        elif G.get(node)[0] != typ:  # type: ignore
            continue

        visited.add(node)
        VISITED.add(node)
        edges += G.get(node)[1]  # type: ignore
        queue.extend(get_neighbors(node, G))

    return len(visited) * edges


def blob(start: tuple, typ: str) -> set:
    global VISITED
    queue: deque = deque([start])
    visited: set = set()

    while queue:
        node = queue.pop()
        if node in visited:
            continue
        elif G.get(node)[0] != typ:  # type: ignore
            continue

        visited.add(node)
        VISITED.add(node)
        queue.extend(get_neighbors(node, G))

    return visited


def unique(nums: list) -> int:
    tot = 0
    sort = sorted(nums)
    deltas = []
    for i in range(1, len(sort)):
        deltas.append(sort[i] - sort[i - 1])
    return len(filterl(lambda x: x != 1, deltas)) + 1


def blob_edges(group: set) -> int:
    up = defaultdict(list)
    down = defaultdict(list)
    left = defaultdict(list)
    right = defaultdict(list)

    # edge = filter(lambda x: x[1] != 0, group)
    for e in list(group):
        x, y = e
        if G.get((x - 1, y), [False])[0] != G.get(e, [True])[0]:  # type: ignore
            up[x].append(y)
        if G.get((x + 1, y), [False])[0] != G.get(e, [True])[0]:  # type: ignore
            down[x].append(y)

        if G.get((x, y + 1), [False])[0] != G.get(e, [True])[0]:  # type: ignore
            right[y].append(x)
        if G.get((x, y - 1), [False])[0] != G.get(e, [True])[0]:  # type: ignore
            left[y].append(x)
    tot = 0
    for u in up.values():
        tot += unique(u)

    for d in down.values():
        tot += unique(d)

    for l in left.values():
        tot += unique(l)

    for r in right.values():
        tot += unique(r)

    # print(list(up.values()))
    # print(list(down.values()))
    # print(list(left.values()))
    # print(list(right.values()))
    # print()

    return tot


def part_1() -> int:
    tot = 0
    for start in G.keys():
        if start not in VISITED:
            tot += size(start, input[start[0]][start[1]])

    return tot


def part_2() -> int:
    global VISITED
    VISITED = set()
    tot = 0
    for start in G.keys():
        if start not in VISITED:
            group = blob(start, input[start[0]][start[1]])
            edge = blob_edges(group)
            # print(G.get(start)[0]) #type: ignore
            # print(edge,end= "  ")
            # print(len(group))
            # print()
            tot += (len(group) * edge)

    return tot


print(part_1())
print(part_2())
