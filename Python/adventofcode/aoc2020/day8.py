from collections import namedtuple

Instruction = namedtuple("Instruction", "opcode, operand")


class SantaClaws:
    def __init__(self, program):
        self.program = program
        self.pc = 0
        self.acc = 0
        self.halted = False

        self.last_address = len(self.program) - 1

    def step(self):
        if self.pc < 0 or self.pc > self.last_address:
            self.halted = True
            return
        instruction = self.program[self.pc]
        if instruction.opcode == "acc":
            self.acc += instruction.operand
            self.pc += 1
        elif instruction.opcode == "jmp":
            self.pc += instruction.operand
        elif instruction.opcode == "nop":
            self.pc += 1

    def run(self):
        while not self.halted:
            self.step()


def parse_program(lines):
    program = []
    for line in lines:
        if line:
            (opcode, str_operand) = line.split(" ")
            operand = int(str_operand)
            program.append(Instruction(opcode, operand))
    return program


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
