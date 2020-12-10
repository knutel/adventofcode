def part1(lines):
    lines = lines[:]
    mine = max(lines) + 3
    lines.append(mine)
    lines.append(0)
    lines.sort()
    diffs = [b - a for (a, b) in zip(lines, lines[1:])]
    ones = [d for d in diffs if d == 1]
    threes = [d for d in diffs if d == 3]
    return len(ones) * len(threes)


def build(adapters, start, memoized):
    if start == len(adapters) - 1:
        memoized[start] = 1
        return

    l = start + 1
    h = min(len(adapters), l + 3)
    candidates = [i for i in range(l, h) if adapters[i] - adapters[start] <= 3]
    if len(candidates) == 0:
        memoized[start] = 0
        return

    combos = 0
    for candidate in candidates:
        if candidate not in memoized:
            build(adapters, candidate, memoized)
        if candidate in memoized:
            combos += memoized[candidate]
    memoized[start] = combos


def part2(lines):
    mine = max(lines) + 3
    lines.append(mine)
    lines.append(0)
    lines.sort()
    memoized = {}
    build(lines, 0, memoized)
    return memoized[0]


if __name__ == "__main__":
    lines = [int(line.strip()) for line in open("input10.txt", "r").read().strip().splitlines()]
    print(part1(lines))
    print(part2(lines))
