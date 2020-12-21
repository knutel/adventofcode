from collections import defaultdict


def parse(lines):
    foods = []
    for line in lines:
        ingredients, allergens = [l[:-1] for l in line.split("(")]
        ingredients = set((ing for ing in ingredients.split(" ")))
        allergens = set((allergen.strip() for allergen in allergens[len("contains"):].split(",")))
        foods.append((ingredients, allergens))
    return foods


def get_allergens(foods):
    locked = {}
    candidates = defaultdict(lambda: set())
    for (ingredients, allergens) in foods:
        for allergen in allergens:
            if allergen in candidates:
                possible = candidates[allergen].intersection(ingredients)
                candidates[allergen] = possible
            else:
                candidates[allergen].update(ingredients)

    while candidates:
        new_candidates = {}
        for candidate, possible in candidates.items():
            if len(possible) == 1:
                locked[candidate] = possible.pop()
        for candidate, possible in candidates.items():
            for locked_value in locked.values():
                if locked_value in possible:
                    possible.remove(locked_value)
            if possible:
                new_candidates[candidate] = possible
        candidates = new_candidates

    return locked


def part1(lines):
    count = 0
    foods = parse(lines)
    allergens = get_allergens(foods)
    for (ingredients, _) in foods:
        for ingredient in ingredients:
            if ingredient not in allergens.values():
                count += 1
    return count


def part2(lines):
    foods = parse(lines)
    allergens = list(get_allergens(foods).items())
    allergens.sort(key=lambda x: x[0])
    return ",".join((a[1] for a in allergens))


if __name__ == "__main__":
    lines = [line.strip() for line in open("input21.txt", "r").read().strip().splitlines()]
    print(part1(lines))
    print(part2(lines))
