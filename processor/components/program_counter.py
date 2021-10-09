class ProgramCounter:
    
    def __init__(self) -> None:
        self.address = 0

    def increment(self):
        self.address += 1
