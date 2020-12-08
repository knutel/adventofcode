from adventofcode.aoc2020.santaclaws import SantaClaws, parse_program, Instruction


def run_program_with_loop_detection(program):
    cpu = SantaClaws(program)
    visited = set()
    while cpu.pc not in visited and not cpu.halted:
        visited.add(cpu.pc)
        cpu.step()
    return cpu.pc, cpu.acc


def part1(lines):
    program = parse_program(lines)
    (pc, acc) = run_program_with_loop_detection(program)
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
        (pc, acc) = run_program_with_loop_detection(mutated_program)
        if pc > len(mutated_program) - 1:
            return acc
    return None


if __name__ == "__main__":
    lines = [line.strip() for line in open("input8.txt", "r").readlines()]

    print(part1(lines))
    print(part2(lines))
