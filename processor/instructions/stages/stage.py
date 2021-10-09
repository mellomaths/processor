from processor.components.datapath import Datapath


class Stage:

    def __init__(self, next_stage) -> None:
        self.next_stage = next_stage

    def execute(self, datapath: Datapath) -> bool:
        if self.next_stage is None:
            return False

        return self.next_stage.execute(datapath)
        