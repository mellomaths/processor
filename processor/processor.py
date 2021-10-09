from memory.memory import Memory
from processor.components.datapath import Datapath
from processor.instructions.instruction_execution_chain import InstructionExecutionChain


class Processor:

    def __init__(self, bits: int, memory: Memory) -> None:
        self.instruction_execution_chain = InstructionExecutionChain()
        self.datapath = Datapath(bits, memory)

    def execute(self):
        self.instruction_execution_chain.execute(self.datapath)
