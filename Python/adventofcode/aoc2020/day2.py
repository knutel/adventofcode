def part1(lines):
    valid = 0
    for line in lines:
        (policy, password) = line.split(":")
        (lrange, character) = policy.split(" ")
        (l, h) = lrange.split("-")
        (l, h) = (int(l), int(h))
        count = sum([1 for c in password if c == character])
        if l <= count <= h:
            valid += 1
    return valid


def part2(lines):
    valid = 0
    for line in lines:
        (policy, password) = line.split(":")
        (lrange, character) = policy.split(" ")
        (l, h) = lrange.split("-")
        (l, h) = (int(l) - 1, int(h) - 1)
        # print(l, h, password[l], password[h], line)
        password = password.strip()

        if (password[l] == character and password[h] != character) or (
                password[l] != character and password[h] == character):
            valid += 1
            # print(line)
    return valid


if __name__ == "__main__":
    lines = open("input2.txt", "r").read().strip().splitlines()

    print(part1(lines))
    print(part2(lines))
