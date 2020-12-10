def part1(lines):
    return lines.count("(") - lines.count(")")


def part2(lines):
    floor = 0
    position = 0
    while floor != -1:
        position += 1
        floor = part1(lines[:position])
    return position


if __name__ == "__main__":
    print(part1(lines))
    print(part2(lines))
