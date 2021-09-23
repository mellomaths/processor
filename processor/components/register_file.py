from processor.components.register import Register


class RegisterFile:
    
    def __init__(self, bits: int) -> None:
        self.size = bits
        self.registers = [Register(i) for i in range(bits)]


    def get_register(self, register_number: int) -> Register:
        return self.registers[register_number]


    def read(self, register_number: int) -> int:
        return self.registers[register_number].read()

    def write(self, register_number: int, data: int) -> None:
        self.registers[register_number].write(data)
