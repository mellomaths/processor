from processor.instructions.set.instruction_set import Instruction
from program.program import Program
from processor.process import Process


class Memory:

    def __init__(self, size: int) -> None:
        self.size = size
        self.process = None

    def load_program(self, program: Program):
        pid = 0
        self.process = Process(pid, program)

    def get_instruction(self, address: int) -> Instruction:
        return self.process.program.instructions[address]
