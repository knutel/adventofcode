def part1(lines):
    x, y, d = 0, 0, 0
    for line in lines:
        (op, param) = (line[0], int(line[1:]))
        if op == "n":
            y -= param
        elif op == "s":
            y += param
        elif op == "w":
            x -= param
        elif op == "e":
            x += param
        elif op == "l":
            c = param / 90
            d = (d + 4 - c) % 4
        elif op == "r":
            c = param / 90
            d = int((d + c) % 4)
        elif op == "f":
            if d == 0:
                x += param
            elif d == 1:
                y += param
            elif d == 2:
                x -= param
            elif d == 3:
                y -= param
    return abs(x) + abs(y)


def rotate(x, y, c):
    for _ in range(c):
        x, y = y, -x
    return x, y


def part2(lines):
    x, y = 10, -1
    sx, sy = 0, 0
    for line in lines:
        (op, param) = (line[0], int(line[1:]))
        if op == "n":
            y -= param
        elif op == "s":
            y += param
        elif op == "w":
            x -= param
        elif op == "e":
            x += param
        elif op == "l":
            c = param // 90
            (x, y) = rotate(x, y, c)
        elif op == "r":
            c = 4 - param // 90
            (x, y) = rotate(x, y, c)
        elif op == "f":
            sx += x * param
            sy += y * param
    return abs(sx) + abs(sy)


if __name__ == "__main__":
    lines = [line.strip().lower() for line in open("input12.txt", "r").read().strip().splitlines()]
    print(part1(lines))
    print(part2(lines))
