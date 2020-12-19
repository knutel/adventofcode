class Either:
    def __init__(self, r, children):
        self.r = r
        self.children = children

    def __str__(self):
        return "Either[" + ", ".join([str(c) for c in self.children]) + "]"

    def consume(self, lookup, message):
        for e in self.children:
            ok, rest = e.consume(lookup, message)
            if ok:
                return True, rest
        return False, message


class Sequence:
    def __init__(self, children):
        self.children = children

    def __str__(self):
        return "Sequence[" + ", ".join([str(c) for c in self.children]) + "]"

    def consume(self, lookup, message):
        rest = message
        for s in self.children:
            ok, rest = s.consume(lookup, rest)
            if not ok:
                return False, message
            if len(rest) == 0:
                break
        return True, rest


class Leaf:
    def __init__(self, r, value):
        self.r = r
        self.value = value

    def __str__(self):
        return f"Leaf({self.value}"

    def consume(self, lookup, message):
        if self.value == message[0]:
            return True, message[1:]
        else:
            return False, message


class Loop:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"Loop({self.value})"

    def consume(self, lookup, message):
        return lookup[self.value].consume(lookup, message)


def parse(lines):
    raw_rules = []
    messages = []
    rules_done = False
    for line in lines:
        if not rules_done:
            if line:
                raw_rules.append(line)
            else:
                rules_done = True
        else:
            messages.append(line)
    rules = {}
    raw_rules.reverse()
    for raw in raw_rules:
        n, m = raw.split(":")
        if "\"" in m:
            rules[int(n)] = m.strip()[1]
        else:
            rules[int(n)] = [[int(k) for k in r.strip().split(" ")] for r in m.split("|")]
    return rules, messages


def build_tree(r, rules, visited, lookup):
    if r in visited:
        return Loop(r)
    rule = rules[r]
    visited = visited[:]
    visited.append(r)
    if isinstance(rule, list):
        tree = Either(r, [Sequence([build_tree(s, rules, visited, lookup) for s in option]) for option in rule])
        lookup[r] = tree
        return tree
    else:
        tree = Leaf(r, rule)
        lookup[r] = tree
        return tree


def part1(lines):
    rules, messages = parse(lines)
    lookup = {}
    tree = build_tree(0, rules, [], lookup)
    return sum((1 for m in messages if tree.consume(lookup, m) == (True, '')))


def part2(lines):
    lines = ["8: 42 | 42 8", "11: 42 31 | 42 11 31"] + lines
    rules, messages = parse(lines)
    lookup = {}
    tree = build_tree(0, rules, [], lookup)
    return sum((1 for m in messages if tree.consume(lookup, m) == (True, '')))


if __name__ == "__main__":
    lines = [line.strip() for line in open("input19.txt", "r").read().strip().splitlines()]
    print(part1(lines))
    print(part2(lines))
