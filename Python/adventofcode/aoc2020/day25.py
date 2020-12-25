def find_loop_size(pk):
    candidate_pk = 1
    loop_size = 0
    while candidate_pk != pk:
        candidate_pk *= 7
        candidate_pk %= 20201227
        loop_size += 1
    return loop_size


def transform(subject, loop_size):
    sk = 1
    for _ in range(loop_size):
        sk *= subject
        sk %= 20201227
    return sk


def part1(lines):
    c_pk, d_pk = [int(l) for l in lines]
    c_loop_size = find_loop_size(c_pk)
    d_loop_size = find_loop_size(d_pk)
    sk_1 = transform(c_pk, d_loop_size)
    sk_2 = transform(d_pk, c_loop_size)
    assert sk_1 == sk_2
    return sk_1


if __name__ == "__main__":
    lines = [line.strip() for line in open("input25.txt", "r").read().strip().splitlines()]
    print(part1(lines))
