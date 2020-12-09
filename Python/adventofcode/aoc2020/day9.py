def part1(lines, preamble=25):
    start = preamble
    for pos in range(start, len(lines)):
        lookup = set(lines[pos - preamble:pos])
        ok = False
        for prev in lookup:
            diff = lines[pos] - prev
            if diff in lookup and diff != prev:
                ok = True
        if not ok:
            return lines[pos]


def part2(lines):
    n = part1(lines)
    length = 0
    while length < len(lines):
        length += 1
        sums = [sum(lines[i - length:i]) for i in range(length, len(lines))]
        if n in sums:
            i = sums.index(n)
            break
    low = min(lines[i:i+length])
    high = max(lines[i:i+length])
    return low + high


if __name__ == "__main__":
    lines = [int(line.strip()) for line in open("input9.txt", "r").read().strip().splitlines()]
    print(part1(lines))
    print(part2(lines))
