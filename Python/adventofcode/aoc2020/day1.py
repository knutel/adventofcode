def part1(numbers):
    for first in numbers:
        for second in set(numbers) - set([first]):
            if first + second == 2020:
                return first * second


def part2(numbers):
    for first in numbers:
        for second in set(numbers) - set([first]):
            third = 2020 - first - second
            if third in numbers:
                return first * second * third


if __name__ == "__main__":
    numbers = [int(n) for n in open("input1.txt", "r").read().strip().splitlines()]
    print(part1(numbers))
    print(part2(numbers))
