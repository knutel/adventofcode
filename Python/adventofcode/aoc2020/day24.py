from collections import defaultdict
from enum import Enum


class Dir(Enum):
    e = 0
    se = 1
    sw = 2
    w = 3
    nw = 4
    ne = 5


def flip(path, tiles):
    (x, y) = (0, 0)
    for p in path:
        if p == Dir.e:
            x += 2
        elif p == Dir.se:
            x += 1
            y += 1
        elif p == Dir.sw:
            x -= 1
            y += 1
        elif p == Dir.w:
            x -= 2
        elif p == Dir.nw:
            x -= 1
            y -= 1
        elif p == Dir.ne:
            x += 1
            y -= 1
    tiles[(x, y)] = not tiles[(x, y)]


def get_neighbors(pos, tiles):
    (x0, y0) = pos
    neighbors = set([(x0 + 2, y0), (x0 + 1, y0 + 1), (x0 - 1, y0 + 1), (x0 - 2, y0), (x0 - 1, y0 - 1), (x0 + 1, y0 - 1)])
    return neighbors


def count_black_neighbors(neighbors, tiles):
    return len([1 for n in neighbors if n in tiles and (not tiles[n])])


def get_tiles(lines):
    paths = []
    for line in lines:
        path = []
        while line:
            for d in Dir:
                if line.startswith(d.name):
                    path.append(d)
                    line = line[len(d.name):]
        paths.append(path)
    tiles = defaultdict(lambda: True)
    for path in paths:
        flip(path, tiles)
    return tiles


def part1(lines):
    tiles = get_tiles(lines)
    return len([1 for t in tiles.values() if not t])


def gol(tiles):
    for day in range(100):
        to_flip = []
        new_neighbors = set()
        for pos in tiles.keys():
            neighbors = get_neighbors(pos, tiles)
            new_neighbors.update(set([neighbor for neighbor in neighbors if neighbor not in tiles]))
            black_count = count_black_neighbors(neighbors, tiles)
            if tiles[pos]:
                if black_count == 2:
                    to_flip.append(pos)
            else:
                if black_count == 0 or black_count > 2:
                    to_flip.append(pos)
        for pos in new_neighbors:
            neighbors = get_neighbors(pos, tiles)
            black_count = count_black_neighbors(neighbors, tiles)
            if black_count == 2:
                to_flip.append(pos)
        for pos in to_flip:
            tiles[pos] = not tiles[pos]


def part2(lines):
    tiles = get_tiles(lines)
    gol(tiles)
    return len([1 for t in tiles.values() if not t])


if __name__ == "__main__":
    lines = [line.strip() for line in open("input24.txt", "r").read().strip().splitlines()]
    print(part1(lines))
    print(part2(lines))