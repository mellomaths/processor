from processor.components.datapath import Datapath
from processor.instructions.stages.instruction_fetch_stage import InstructionFetchStage
from processor.instructions.stages.instruction_decode_stage import InstructionDecodeStage
from processor.instructions.stages.execution_stage import ExecutionStage
from processor.instructions.stages.memory_access_stage import MemoryAccessStage
from processor.instructions.stages.write_back_stage import WriteBackStage


class InstructionExecutionChain:

    def __init__(self) -> None:
        self.stages = InstructionFetchStage(InstructionDecodeStage(ExecutionStage(MemoryAccessStage(WriteBackStage(None)))))

    def execute(self, datapath: Datapath):
        self.stages.execute(datapath)
