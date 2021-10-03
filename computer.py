from processor.instructions.set.load import Load
from program.program import Program
from processor.processor import Processor
from memory.memory import Memory


class Computer:

    def __init__(self) -> None:
        self.processor = Processor(32)
        self.memory = Memory(1024)

    def start_program(self, program: Program):
        self.processor.execute()


if __name__ == "__main__":
    computer = Computer()
    program = Program(128)
    program.set_variable("a", 12)
    program.set_variable("b", 18)
    program.set_instruction(Load(1, 0))
    program.set_instruction(Load(2, 4))
    computer.start_program(program)
