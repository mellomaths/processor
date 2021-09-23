from processor.instructions.stages.stage import Stage


class InstructionDecodeStage(Stage):

    def __init__(self, next_stage) -> None:
        super().__init__(next_stage)
    
    def execute(self):
        print('Executing the Instruction Decode Stage')
        return super().execute()
