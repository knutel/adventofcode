from collections import namedtuple, defaultdict
import re

Instruction = namedtuple("Instruction", "opcode, operand1, operand2")

def parse(lines):
    program = []
    for line in lines:
        if line.startswith("mask"):
            opcode, param = line.split("=")
            program.append(Instruction(opcode.strip(), param.strip(), None))
        elif line.startswith("mem"):
            m = re.match(r"mem\[(\d+)\] = (\d+)", line)
            if m:
                program.append(Instruction("mem", int(m.group(1)), int(m.group(2))))
    return program


def part1(lines):
    program = parse(lines)
    mem = defaultdict(lambda: 0)
    mask = None
    for instruction in program:
        if instruction.opcode == "mask":
            mask = instruction.operand1
        elif instruction.opcode == "mem":
            ones = int(mask.replace("x", "0"), 2)
            zeroes = int(mask.replace("x", "1"), 2)
            value = (instruction.operand2 | ones) & zeroes
            mem[instruction.operand1] = value
    return sum(mem.values())


def part2(lines):
    program = parse(lines)
    mem = defaultdict(lambda: 0)
    mask = None
    for instruction in program:
        if instruction.opcode == "mask":
            mask = instruction.operand1
        elif instruction.opcode == "mem":
            ones = int(mask.replace("x", "0"), 2)
            address = instruction.operand1 | ones
            floating = [35 - i for (i, v) in enumerate(mask) if v == "x"]
            for n in range(2 ** len(floating)):
                real_address = address
                for (m, i) in enumerate(floating):
                    if (1 << m) & n == 0:
                        real_address &= ((1 << 36) - 1) ^ (1 << i)
                    else:
                        real_address |= 1 << i
                mem[real_address] = instruction.operand2
    return sum(mem.values())


if __name__ == "__main__":
    lines = [line.strip().lower() for line in open("input14.txt", "r").read().strip().splitlines()]
    print(part1(lines))
    print(part2(lines))
