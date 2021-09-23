class Register:

    def __init__(self, number: int) -> None:
        self.number = number
        self.data = 0

    def read(self) -> int:
        return self.data

    def write(self, data: int) -> None:
        self.data = data