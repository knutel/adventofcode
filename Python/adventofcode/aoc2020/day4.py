def split_passports(lines):
    current_passport = []
    passports = []
    for line in lines:
        line = line.strip()
        if line:
            current_passport.append(line)
        else:
            passports.append(" ".join(current_passport))
            current_passport = []
    if current_passport:
        passports.append(" ".join(current_passport))
    return passports


def make_prop(p):
    split = p.split(":")
    if len(split) == 1:
        return split[0], ""
    else:
        return split[0], split[1]


def parse_passport(unparsed):
    properties = [make_prop(prop) for prop in unparsed.split(" ")]
    return dict(properties)


def parse_passports(unparsed):
    return [parse_passport(p) for p in unparsed]


FIELDS = set([line.strip().split(" ")[0] for line in """byr (Birth Year)
    iyr (Issue Year)
    eyr (Expiration Year)
    hgt (Height)
    hcl (Hair Color)
    ecl (Eye Color)
    pid (Passport ID)
    cid (Country ID)""".splitlines()])


def check_valid(p):
    missing = FIELDS - set(p.keys())
    return (len(missing) == 1 and "cid" in missing) or len(missing) == 0


def part1(lines):
    split = split_passports(lines)
    parsed = parse_passports(split)
    is_valid = [p for p in parsed if check_valid(p)]
    return len(is_valid)


def check_fields(p):
    try:
        for (key, value) in p.items():
            if key == "byr":
                v = int(value)
                if v < 1920 or v > 2002:
                    return False
            elif key == "iyr":
                v = int(value)
                if v < 2010 or v > 2020:
                    return False
            elif key == "eyr":
                v = int(value)
                if v < 2020 or v > 2030:
                    return False
            elif key == "hgt":
                if value.endswith("cm"):
                    v = int(value[:-2])
                    if v < 150 or v > 193:
                        return False
                elif value.endswith("in"):
                    v = int(value[:-2])
                    if v < 59 or v > 76:
                        return False
                else:
                    return False
            elif key == "hcl":
                if value[0] == "#":
                    if len([c for c in value[1:] if c in "0123456789abcdef"]) != 6:
                        return False
                else:
                    return False
            elif key == "ecl":
                if value not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
                    return False
            elif key == "pid":
                v = int(value)
                if len(value) != 9:
                    return False
            elif key == "cid":
                pass
    except ValueError as e:
        return False
    return True


def check_valid2(passports):
    p = [passport for passport in passports if check_valid(passport)]
    p = [passport for passport in p if check_fields(passport)]
    return len(p)


def part2(lines):
    split = split_passports(lines)
    parsed = parse_passports(split)
    return check_valid2(parsed)


if __name__ == "__main__":
    lines = [line.strip() for line in open("input4.txt", "r").readlines()]

    print(part1(lines))

    assert(check_fields({"byr": "2002"}))
    assert(not check_fields({"byr": "2003"}))
    assert(check_fields({"hgt": "60in"}))
    assert(check_fields({"hgt": "190cm"}))
    assert(not check_fields({"hgt": "190in"}))
    assert(not check_fields({"hgt": "190"}))
    assert(check_fields({"hcl": "#123abc"}))
    assert(not check_fields({"hcl": "#123abz"}))
    assert(not check_fields({"hcl": "123abc"}))

    print(part2(lines))

