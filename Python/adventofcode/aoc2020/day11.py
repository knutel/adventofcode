def make_world(lines):
    world = {}
    for (y, line) in enumerate(lines):
        for (x, cell) in enumerate(line):
            world[(x, y)] = cell
    return world


def count_adjacent(world, pos):
    (x, y) = pos
    adjacent = [(x - 1, y), (x - 1, y - 1), (x - 1, y + 1),
                (x, y - 1), (x, y + 1),
                (x + 1, y), (x + 1, y - 1), (x + 1, y + 1)]
    occupied = [p for p in adjacent if p in world and world[p] == "#"]
    return len(occupied)


def gol(world):
    while True:
        new_world = {}
        for (pos, cell) in world.items():
            n = count_adjacent(world, pos)
            if cell == "L" and n == 0:
                cell = "#"
            elif cell == "#" and n >= 4:
                cell = "L"
            elif cell == ".":
                cell = "."
            new_world[pos] = cell
        if new_world == world:
            return len([s for s in new_world.values() if s == "#"])
        world = new_world


def count_adjacent_line(world, pos, dx, dy):
    (x, y) = pos
    while True:
        x += dx
        y += dy
        if (x, y) not in world:
            return 0
        cell = world[(x, y)]
        if cell == "L":
            return 0
        elif cell == "#":
            return 1


def count_adjacent2(world, pos):
    (x, y) = pos
    return sum(count_adjacent_line(world, pos, dx, dy) for (dx, dy) in
               [(-1, 0), (-1, -1), (-1, 1), (0, -1), (0, 1), (1, 0), (1, -1), (1, 1)])


def gol2(world):
    while True:
        new_world = {}
        for (pos, cell) in world.items():
            n = count_adjacent2(world, pos)
            if cell == "L" and n == 0:
                cell = "#"
            elif cell == "#" and n >= 5:
                cell = "L"
            elif cell == ".":
                cell = "."
            new_world[pos] = cell
        if new_world == world:
            return len([s for s in new_world.values() if s == "#"])
        world = new_world


def part1(lines):
    world = make_world(lines)
    return gol(world)


def part2(lines):
    world = make_world(lines)
    return gol2(world)


if __name__ == "__main__":
    lines = [line.strip() for line in open("input11.txt", "r").read().strip().splitlines()]
    print(part1(lines))
    print(part2(lines))
