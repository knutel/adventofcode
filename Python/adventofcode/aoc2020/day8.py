from collections import namedtuple

Instruction = namedtuple("Instruction", "opcode, operand")

def parse_program(lines):
    program = []
    for line in lines:
        if line:
            (opcode, str_operand) = line.split(" ")
            operand = int(str_operand)
            program.append(Instruction(opcode, operand))
    return program

def run_program(program):
    pc = 0
    acc = 0
    visited = set()
    while pc not in visited and pc < len(program):
        instruction = program[pc]
        visited.add(pc)
        if instruction.opcode == "acc":
            acc += instruction.operand
            pc += 1
        elif instruction.opcode == "jmp":
            pc += instruction.operand
        elif instruction.opcode == "nop":
            pc += 1
    return pc, acc


def part1(lines):
    program = parse_program(lines)
    (pc, acc) = run_program(program)
    return acc


def part2(lines):
    program = parse_program(lines)
    nops_and_jmps = [offset for (offset, i) in enumerate(program) if i.opcode == "jmp" or i.opcode == "nop"]
    for mutate_instruction in nops_and_jmps:
        mutated_program = program[:]
        instruction = mutated_program[mutate_instruction]
        if instruction.opcode == "jmp":
            mutated_program[mutate_instruction] = Instruction("nop", instruction.operand)
        elif instruction.opcode == "nop":
            mutated_program[mutate_instruction] = Instruction("jmp", instruction.operand)
        (pc, acc) = run_program(mutated_program)
        if (pc > len(mutated_program) - 1):
            return acc
    return None

if __name__ == "__main__":
    lines = [line.strip() for line in open("input8.txt", "r").readlines()]

    print(part1(lines))
    print(part2(lines))
