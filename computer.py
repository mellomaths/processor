from processor.instructions.set.instruction_set import Instruction, InstructionSet
from processor.instructions.set.load import Load
from program.program import Program
from processor.processor import Processor
from memory.memory import Memory


class Computer:

    def __init__(self) -> None:
        self.memory = Memory(1024)
        self.processor = Processor(32, self.memory)

    def start_program(self, program: Program):
        self.memory.load_program(program)
        self.processor.execute()


if __name__ == "__main__":
    computer = Computer()
    program = Program(128)
    program.set_variable("a", 12)
    program.set_variable("b", 18)
    program.set_instruction(Instruction(InstructionSet.LW, Load(1, "a")))
    program.set_instruction(Instruction(InstructionSet.LW, Load(2, "b")))
    computer.start_program(program)
