from functools import reduce


def count_trees(forrest, dx, dy):
    (x, y) = (0, 0)
    trees = 0
    while y < len(forrest):
        x = (x + dx) % len(forrest[0])
        y += dy
        if y < len(forrest) and forrest[y][x] == "#":
            trees += 1

    return trees


if __name__ == "__main__":
    lines = [line.strip() for line in open("input3.txt", "r").readlines()]
    print(count_trees(lines, 3, 1))
    print(reduce(lambda a, b: a * b, map(lambda slope: count_trees(lines, *slope), [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]), 1))
