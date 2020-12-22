def parse(lines):
    p1 = []
    p2 = []

    for line in lines:
        if "Player 1:" in line:
            p = p1
            continue
        if "Player 2:" in line:
            p = p2
            continue
        if line:
            p.append(int(line))
    return p1, p2


def part1(lines):
    p1, p2 = parse(lines)
    while p1 and p2:
        c1 = p1.pop(0)
        c2 = p2.pop(0)
        if c1 > c2:
            p1.append(c1)
            p1.append(c2)
        else:
            p2.append(c2)
            p2.append(c1)
    p = p1 + p2
    return sum((c * (len(p) - i) for i, c in enumerate(p)))


def recursive_play(game, p1, p2):
    seen = set()
    game[0] += 1
    this_game = game[0]
    decks = (tuple(p1), tuple(p2))
    while p1 and p2:
        if decks in seen:
            return 1
        seen.add(decks)
        c1 = p1.pop(0)
        c2 = p2.pop(0)
        if len(p1) >= c1 and len(p2) >= c2:
            winner = recursive_play(game, p1[:c1], p2[:c2])
        else:
            if c1 > c2:
                winner = 1
            else:
                winner = 2
        if winner == 1:
            p1.append(c1)
            p1.append(c2)
        else:
            p2.append(c2)
            p2.append(c1)
        decks = (tuple(p1), tuple(p2))

    if this_game == 1:
        return p1, p2
    else:
        return 1 if p1 else 2


def part2(lines):
    p1, p2 = parse(lines)
    p1, p2 = recursive_play([0], p1, p2)
    p = p1 + p2
    return sum((c * (len(p) - i) for i, c in enumerate(p)))


if __name__ == "__main__":
    lines = [line.strip() for line in open("input22.txt", "r").read().strip().splitlines()]
    print(part1(lines))
    print(part2(lines))
