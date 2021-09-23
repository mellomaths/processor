from processor.instructions.instruction_execution_chain import InstructionExecutionChain


class Pipeline:

    def __init__(self) -> None:
        self.chain = InstructionExecutionChain()
    
    def execute(self):
        self.chain.execute()
