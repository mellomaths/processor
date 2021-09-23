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
    computer.start_program(program)
