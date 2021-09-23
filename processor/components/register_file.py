class RegisterFile:
    
    def __init__(self, bits: int) -> None:
        self.size = bits
        self.registers = [0 for i in range(bits)]


    def read(self, register_number: int):
        return self.registers[register_number]
