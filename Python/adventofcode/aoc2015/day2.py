def part1(lines):
    total = 0
    for line in lines:
        (l, w, h) = [int(n) for n in line.split("x")]
        (wl, wh, hl) = (l * w, w * h, h * l)
        a = 2 * wl + 2 * wh + 2 * hl + min([wl, wh, hl])
        total += a
    return total


def part2(lines):
    total = 0
    for line in lines:
        (l, w, h) = [int(n) for n in line.split("x")]
        total += l * w * h + 2 * min([l + w, w + h, l + h])
    return total


if __name__ == "__main__":
    lines = [line.strip() for line in open("input2.txt", "r").read().strip().splitlines()]
    print(part1(lines))
    print(part2(lines))
