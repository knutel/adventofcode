import math
from functools import lru_cache


def create_tile(lines):
    return Tile(int(lines[0][5:-1]), lines[1:])


class Tile:
    def __init__(self, id, grid):
        self.id = id
        self.grid = grid

    def rotate_cw(self):
        grid = []
        rev = self.grid[:]
        rev.reverse()
        for l in range(len(rev)):
            grid.append("".join([r[l] for r in rev]))
        return Tile(self.id, grid)

    def flip_v(self):
        grid = [l[::-1] for l in self.grid]
        return Tile(self.id, grid)

    def flip_h(self):
        grid = self.grid[::-1]
        return Tile(self.id, grid)

    def rotate(self, n):
        pass

    def __str__(self):
        return str(self.id) + "\n" + "\n".join(self.grid)

    def right(self):
        return "".join([line[-1] for line in self.grid])

    def left(self):
        return "".join([line[0] for line in self.grid])

    def top(self):
        return self.grid[0]

    def bottom(self):
        return self.grid[-1]


def parse(lines):
    current = []
    tiles = []
    for line in lines:
        if not line:
            tiles.append(create_tile(current))
            current = []
        else:
            current.append(line)
    tiles.append(create_tile(current))
    return tiles


@lru_cache(None)
def get_all_orientations(tile):
    orientations = [tile]
    for n in range(3):
        orientations.append(orientations[-1].rotate_cw())
    for n in range(4):
        orientations.append(orientations[n].flip_v())
        orientations.append(orientations[n].flip_h())
    return orientations


def get_empty_neighbors(pos, grid):
    (x0, y0) = pos
    return [pos1 for pos1 in [(x0 - 1, y0), (x0, y0 - 1), (x0 + 1, y0), (x0, y0 + 1)] if pos1 in grid and grid[pos1] is None]


@lru_cache(None)
def check_fit_h(a, b):
    return a.right() == b.left()


@lru_cache(None)
def check_fit_v(a, b):
    return a.bottom() == b.top()


def tile_fits(tile, pos, grid):
    (x, y) = pos
    left = (x - 1, y)
    if left in grid:
        other = grid[left]
        if other:
            if other.right() != tile.left():
                return False
    right = (x + 1, y)
    if right in grid:
        other = grid[right]
        if other:
            if other.left() != tile.right():
                return False
    above = (x, y - 1)
    if above in grid:
        other = grid[above]
        if other:
            if other.bottom() != tile.top():
                return False
    below = (x, y + 1)
    if below in grid:
        other = grid[below]
        if other:
            if other.top() != tile.bottom():
                return False
    return True


def place(positions, grid, tiles):
    if len(positions) == 0:
        return grid
    pos = positions.pop(0)
    for (i, tile) in enumerate(tiles):
        rest_tiles = tiles.copy()
        rest_tiles.remove(tile)
        for orientation in get_all_orientations(tile):
            if tile_fits(orientation, pos, grid):
                new_grid = grid.copy()
                new_grid[pos] = orientation
                result = place(positions[:], new_grid, rest_tiles)
                if result:
                    return result
    else:
        return None


def arrange(lines):
    tiles = set(parse(lines))
    side = int(math.sqrt(len(tiles)))
    positions = []
    for x in range(side):
        positions.append((x, 0))
    for y in range(1, side):
        positions.append((side - 1, y))
    for x in range(side - 2, -1, -1):
        positions.append((x, side - 1))
    for y in range(side - 2, 0, -1):
        positions.append((0, y))
    for y in range(1, side - 1):
        for x in range(1, side - 1):
            positions.append((x, y))

    grid = {(x, y): None for x in range(side) for y in range(side)}

    result = place(positions, grid, tiles)

    return result, side


def part1(jigsaw, side):
    return jigsaw[(0, 0)].id * jigsaw[(0, side - 1)].id * jigsaw[(side - 1, 0)].id * jigsaw[(side - 1, side - 1)].id


def part2(jigsaw, side):
    tile_side = len(jigsaw[(0, 0)].grid[0])
    joined = []

    for y in range(side):
        for ty in range(1, tile_side - 1):
            l = "".join([jigsaw[(x, y)].grid[ty][1:-1] for x in range(side)])
            joined.append(l)

    t = Tile(0, joined)

    sea_monster = ["                  # ",
                   "#    ##    ##    ###",
                   " #  #  #  #  #  #   "]

    coordinates = []
    for y in range(len(sea_monster)):
        for x in range(len(sea_monster[0])):
            if sea_monster[y][x] == "#":
                coordinates.append((x, y))


    map_width = len(t.grid[0])
    map_height = map_width
    m_width = len(sea_monster[0])
    m_height = len(sea_monster)

    for orientation in get_all_orientations(t):
        found = []
        for top in range(0, map_height - m_height):
            for left in range(0, map_width - m_width):
                for (x, y) in coordinates:
                    xx = x + left
                    yy = y + top
                    if orientation.grid[yy][xx] != "#":
                        break
                else:
                    found.append((left, top))
        if found:
            break

    for (fx, fy) in found:
        for (mx, my) in coordinates:
            s = orientation.grid[my + fy]
            x = mx + fx
            orientation.grid[my + fy] = s[:x] + "O" + s[x+1:]

    print(orientation)

    return len([1 for line in orientation.grid for c in line if c == "#"])


if __name__ == "__main__":
    lines = [line.strip() for line in open("input20.txt", "r").read().strip().splitlines()]
    jigsaw, side = arrange(lines)
    print(part1(jigsaw, side))
    print(part2(jigsaw, side))
