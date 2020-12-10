from collections import defaultdict


def visit(lines, n):
    visited = defaultdict(lambda: 1)
    (xs, ys) = ([0] * n, [0] * n)
    for (x, y) in zip(xs, ys):
        visited[(x, y)] += 1
    for (i, d) in enumerate(lines):
        w = i % n
        if d == ">":
            xs[w] += 1
        elif d == "<":
            xs[w] -= 1
        elif d == "^":
            ys[w] -= 1
        elif d == "v":
            ys[w] += 1
        visited[(xs[w], ys[w])] += 1
    return len(visited)


def part1(lines):
    return visit(lines, 1)


def part2(lines):
    return visit(lines, 2)


if __name__ == "__main__":
    lines = open("input3.txt", "r").read()
    print(part1(lines))
    print(part2(lines))
