import re


def parse_rules(lines):
    rules = {}
    for line in lines:
        m = re.match("(.+) bags contain (.+)", line)
        container = m.group(1)
        contents = [c.strip() for c in m.group(2)[:-1].split(",")]
        sub_containers = []
        for c in contents:
            m = re.match("([0-9]+) ([\w\s]+) bag", c)
            if m:
                sub_containers.append((m.group(2), int(m.group(1))))
        rules[container] = sub_containers
    return rules


def part1(lines):
    rules = parse_rules(lines)
    check_bags = {"shiny gold"}
    golden = set()
    while check_bags:
        new_bags = set()
        for (bag, bags) in rules.items():
            for c in check_bags:
                if c in [b[0] for b in bags]:
                    new_bags.add(bag)
        check_bags = new_bags
        golden = golden.union(new_bags)
    return len(golden)


def get_count(rules, multiplier, bag):
    bags = rules[bag]
    return multiplier + multiplier * sum([get_count(rules, b[1], b[0]) for b in bags])


def part2(lines):
    rules = parse_rules(lines)
    return get_count(rules, 1, "shiny gold") - 1


if __name__ == "__main__":
    lines = [line.strip() for line in open("input7.txt", "r").readlines()]

    print(part1(lines))
    print(part2(lines))
