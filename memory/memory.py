from program.program import Program


class Memory:

    def __init__(self, size: int) -> None:
        self.size = size
        self.buffer = [0 for i in range(size)]


    def load_program(self, program: Program):
        pass
