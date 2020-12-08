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
