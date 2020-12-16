from collections import namedtuple
import re
from functools import reduce

Rule = namedtuple("Rule", "field, intervals")


def parse_rules(lines):
    rules = []
    for line in lines:
        m = re.match(r"(.+): (\d+)-(\d+) or (\d+)-(\d+)", line)
        if m:
            rules.append(Rule(m.group(1), [(int(m.group(2)), int(m.group(3))), (int(m.group(4)), int(m.group(5)))]))
    return rules


def parse_my_ticket(lines):
    return [int(n) for n in lines[0].split(",")]


def parse_nearby_tickets(lines):
    return [[int(n) for n in line.split(",")] for line in lines]


def part1(lines):
    nearby_tickets, _, rules = parse(lines)
    invalid_values = []
    for ticket in nearby_tickets:
        for value in ticket:
            valid = [value in range(interval[0], interval[1] + 1) for rule in rules for interval in rule.intervals]
            if not any(valid):
                invalid_values.append(value)
    return sum(invalid_values)


def parse(lines):
    my_ticket_pos = lines.index("your ticket")
    nearby_tickets_pos = lines.index("nearby tickets")
    rules = parse_rules(lines[:my_ticket_pos - 1].strip().splitlines())
    my_ticket = parse_my_ticket(lines[my_ticket_pos:nearby_tickets_pos - 1].strip().splitlines()[1:])
    nearby_tickets = parse_nearby_tickets(lines[nearby_tickets_pos:].strip().splitlines()[1:])
    return nearby_tickets, my_ticket, rules


def part2(lines):
    nearby_tickets, my_ticket, rules = parse(lines)
    valid_tickets = []
    for ticket in nearby_tickets:
        valid = True
        for value in ticket:
            valid = [value in range(interval[0], interval[1] + 1) for rule in rules for interval in rule.intervals]
            if not any(valid):
                valid = False
                break
        if valid:
            valid_tickets.append(ticket)

    field_candidates = {rule.field: set(range(len(valid_tickets[0]))) for rule in rules}

    for rule in rules:
        for ticket in valid_tickets:
            candidates = field_candidates[rule.field]
            for (column, value) in enumerate(ticket):
                if column in candidates:
                    if not any([value in range(interval[0], interval[1] + 1) for interval in rule.intervals]):
                        candidates.remove(column)

    while True:
        fixed_columns = {}
        for field, columns in field_candidates.items():
            if len(columns) == 1:
                column = list(columns)[0]
                fixed_columns[column] = field
        for field, columns in field_candidates.items():
            for column, fixed_field in fixed_columns.items():
                if field != fixed_field and column in columns:
                    columns.remove(column)
        if len(fixed_columns) == len(field_candidates):
            break

    fields = {field: list(columns)[0] for field, columns in field_candidates.items()}

    return reduce(lambda x, y: x * y, [my_ticket[column] for field, column in fields.items()
                                       if field.startswith("departure")], 1)


if __name__ == "__main__":
    lines = open("input16.txt", "r").read().strip()
    print(part1(lines))
    print(part2(lines))
