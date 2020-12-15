def play_game(line, stop):
    prev = {}
    current = {}
    line = [int(l) for l in line.split(",")]
    turn = 1
    for l in line:
        current[l] = turn
        turn += 1
        last = l
    while turn <= stop:
        if last in prev:
            n = current[last] - prev[last]
        else:
            n = 0
        if n in current:
            prev[n] = current[n]
        current[n] = turn
        last = n
        turn += 1
    return n


def part1(line):
    return play_game(line, 2020)


def part2(line):
    return play_game(line, 30000000)


if __name__ == "__main__":
    line = open("input15.txt", "r").read().strip()
    print(part1(line))
    print(part2(line))
