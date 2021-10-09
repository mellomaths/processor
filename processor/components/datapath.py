from memory.memory import Memory
from processor.components.alu import ALU
from processor.components.control_unit import ControlUnit
from processor.components.register_file import RegisterFile
from processor.components.program_counter import ProgramCounter 


class Datapath:
    
    def __init__(self, bits: int, memory: Memory) -> None:
        self.register_file = RegisterFile(bits)
        self.program_counter = ProgramCounter()
        self.control_unit = ControlUnit()
        self.ALU = ALU()
        self.memory = memory
