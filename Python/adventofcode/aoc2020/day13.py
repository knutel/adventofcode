def part1(lines):
    arrival = int(lines[0])
    schedules = [int(l) for l in lines[1].split(",") if l != 'x']
    departed = [s * (arrival // s) for s in schedules]
    next = [d + s for (d, s) in zip(departed, schedules)]
    too_late = [arrival - d for d in departed]
    too_early = [n - arrival for n in next]
    shortest_wait = min(too_early)
    smallest_miss = min(too_late)
    if smallest_miss == 0:
        i = too_late.index(0)
    else:
        i = too_early.index(shortest_wait)

    return schedules[i] * (next[i] - arrival)


def part2(lines):
    schedules = [(i, int(l)) for (i, l) in enumerate(lines[1].split(",")) if l != 'x']
    step = schedules[0][1]
    n = 0
    for (nn, m) in schedules[1:]:
        while True:
            if (n + nn) % m == 0:
                break
            n += step
        step = step * m

    return n


if __name__ == "__main__":
    lines = [line.strip().lower() for line in open("input13.txt", "r").read().strip().splitlines()]
    print(part1(lines))
    print(part2(lines))
