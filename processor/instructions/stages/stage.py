class Stage:

    def __init__(self, next_stage) -> None:
        self.next_stage = next_stage

    def execute(self):
        if self.next_stage is None:
            return

        self.next_stage.execute()
        