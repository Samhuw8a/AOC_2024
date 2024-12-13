from utils.all import *

rinput = read_input_line(13, sep="\n\n")
# rinput = read_input_line("test_13", sep="\n\n")
input = mapl(lambda x: mapl(integers, x.split("\n")), rinput)


def cost(n: tuple) -> int:
    return n[0] * 3 + n[1]


def part_1() -> int:
    tot = 0
    for a_button, b_button, result in input:
        # max_x = (result[0] // max(a_button[0], b_button[0])) + 1
        max_x = 100
        possible = []
        for a in range(1, max_x + 1):
            for b in range(1, max_x + 1):
                if a_button[0] * a + b_button[0] * b == result[0]:
                    if a_button[1] * a + b_button[1] * b == result[1]:
                        possible.append((a, b))
        if len(possible):
            tot += min(map(cost, possible))

    return tot


def part_2() -> int:
    tot = 0
    for a_button, b_button, result in input:
        result = mapl(lambda x: x + 10000000000000, result)
        det_a = a_button[0] * b_button[1] - a_button[1] * b_button[0]

        det_a_ = result[0] * b_button[1] - result[1] * b_button[0]

        det_b_ = a_button[0] * result[1] - a_button[1] * result[0]

        a = det_a_ / det_a
        b = det_b_ / det_a

        if a.is_integer() and b.is_integer():
            tot += a * 3 + b

    return tot


print(part_1())
print(part_2())
