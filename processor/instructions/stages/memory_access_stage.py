from processor.components.datapath import Datapath
from processor.instructions.stages.stage import Stage


class MemoryAccessStage(Stage):

    def __init__(self, next_stage: Stage) -> None:
        super().__init__(next_stage)
    
    def execute(self, datapath: Datapath):
        return super().execute(datapath)
