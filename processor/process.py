from program.program import Program


class Process:

    def __init__(self, id: int, program: Program) -> None:
        self.id = id
        self.program = program
