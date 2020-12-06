def get_seat_id(parts):
    number = parts.replace("F", "0").replace("B", "1").replace("L", "0").replace("R", "1")
    return int(number, 2)


def part1(lines):
    return max([get_seat_id(line) for line in lines])


def part2(lines):
    first = min([get_seat_id(line) for line in lines])
    last = max([get_seat_id(line) for line in lines])
    all_seats = set(range(first, last + 1))
    used_seats = set([get_seat_id(line) for line in lines])
    missing = all_seats - used_seats
    return missing


if __name__ == "__main__":
    lines = [l.strip() for l in open("input5.txt", "r").readlines()]
    assert(get_seat_id("FBFBBFFRLR") == 357)
    print(part1(lines))
    print(part2(lines))
