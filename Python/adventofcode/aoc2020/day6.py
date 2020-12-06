def split_groups(lines):
    current_group = []
    groups = []
    for line in lines:
        line = line.strip()
        if line:
            current_group.append(line)
        else:
            groups.append(current_group)
            current_group = []
    if current_group:
        groups.append(current_group)
    return groups


def part1(lines):
    groups = split_groups(lines)
    count = 0
    for group in groups:
        answers = set()
        for person in group:
            answers = answers.union(set(person))
        count += len(answers)
    return count


def part2(lines):
    groups = split_groups(lines)
    count = 0
    for group in groups:
        answers = set(group[0])
        for person in group:
            answers = answers.intersection(set(person))
        count += len(answers)
    return count


if __name__ == "__main__":
    lines = [line.strip() for line in open("input6.txt", "r").readlines()]

    print(part1(lines))
    print(part2(lines))
