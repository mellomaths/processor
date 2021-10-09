from processor.components.datapath import Datapath
from processor.instructions.stages.stage import Stage


class InstructionFetchStage(Stage):

    def __init__(self, next_stage: Stage) -> None:
        super().__init__(next_stage)
    
    def execute(self, datapath: Datapath):
        print('Fetching instruction')
        instruction_address = datapath.program_counter.address
        instruction = datapath.memory.get_instruction(instruction_address)
        if (instruction is None):
            self.next_stage = None

        print(f'Instruction {instruction.type} fetched.')

        datapath.register_file.set_instruction(instruction)
        datapath.program_counter.increment()
        return super().execute(datapath)
