def make_world(lines):
    world = {}
    for (y, line) in enumerate(lines):
        for (x, cell) in enumerate(line):
            world[(x, y, 0, 0)] = cell
    return world


def get_adjacent(pos):
    (x, y, z, w) = pos
    adjacent = []
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            for dz in [-1, 0, 1]:
                for dw in [-1, 0, 1]:
                    if not (dx == 0 and dy == 0 and dz == 0 and dw == 0):
                        adjacent.append((x + dx, y + dy, z + dz, w + dw))
    return adjacent

def print_world(world):
    x0 = min([p[0] for p in world])
    x1 = max([p[0] for p in world])
    y0 = min([p[1] for p in world])
    y1 = max([p[1] for p in world])
    z0 = min([p[2] for p in world])
    z1 = max([p[2] for p in world])
    w0 = min([p[3] for p in world])
    w1 = max([p[3] for p in world])
    for w in range(w0, w1 + 1):
        for z in range(z0, z1 + 1):
            print(f"z={z}, w={w}")
            for y in range(y0, y1 + 1):
                print("".join([world[(x, y, z, w)] if (x, y, z, w) in world else " " for x in range(x0, x1 + 1)]))
            print()

def gol(world, generations):
    print(world)
    generation = 0
    print("Generation", generation)
    print_world(world)
    while True:
        generation += 1
        new_world = {}
        checklist = set()
        for (pos, cell) in world.items():
            if cell == "#":
                adjacent = get_adjacent(pos)
                checklist.update(adjacent)
                checklist.add(pos)
        print("Checklist", checklist)
        for (pos, cell) in [(pos, world[pos] if pos in world else ".") for pos in checklist]:
            adjacent = get_adjacent(pos)
            occupied = [p for p in adjacent if p in world and world[p] == "#"]
            n = len(occupied)
            #print(n)
            #print(adjacent)
            if cell == "." and n == 3:
                cell = "#"
                new_world[pos] = cell
            elif cell == "#" and not (n == 2 or n == 3):
                cell = "."
                new_world[pos] = cell
        world.update(new_world)
        print("Generation", generation)
        print_world(world)
        if generation == generations:
            break
    return sum((1 for c in world.values() if c == "#"))






def part2(lines):
    world = make_world(lines)
    return gol(world, 6)


if __name__ == "__main__":
    lines = [line.strip() for line in open("input17.txt", "r").read().strip().splitlines()]
    print(part2(lines))
