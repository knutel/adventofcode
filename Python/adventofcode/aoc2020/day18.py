from parsita import *


class ExpressionParsers(TextParsers):
    number = reg(r"[0-9]+") > int
    part = "(" >> expression << ")" | number

    expression = part & rep(lit("+", "*") & part)


class ExpressionParsers2(TextParsers):
    number = reg(r"[0-9]+") > int
    part = "(" >> expression << ")" | number
    plus = part & rep(lit("+") & part)

    expression = plus & rep(lit("*") & plus)


def parse(line):
    result = ExpressionParsers.expression.parse(line)
    return result.value


def parse2(line):
    result = ExpressionParsers2.expression.parse(line)
    return result.value


def evaluate(expression):
    if isinstance(expression, list):
        value, subs = expression
        value = evaluate(value)
    else:
        return expression

    for sub in subs:
        op, subsub = sub
        if op == "+":
            value += evaluate(subsub)
        elif op == "*":
            value *= evaluate(subsub)
    return value


def part1(lines):
    value = 0
    for line in lines:
        expression = parse(line)
        value += evaluate(expression)
    return value


def part2(lines):
    value = 0
    for line in lines:
        expression = parse2(line)
        value += evaluate(expression)
    return value


if __name__ == "__main__":
    lines = [line.strip() for line in open("input18.txt", "r").read().strip().splitlines()]
    print(part1(lines))
    print(part2(lines))
