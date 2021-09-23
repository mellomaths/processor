from processor.components.register_file import RegisterFile
from processor.instructions.instruction_execution_chain import InstructionExecutionChain


class Processor:

    def __init__(self, bits: int) -> None:
        self.instruction_execution_chain = InstructionExecutionChain()
        self.register_file = RegisterFile(bits)

    def execute(self):
        self.instruction_execution_chain.execute()
