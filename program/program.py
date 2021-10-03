class Program:

    def __init__(self, size: int) -> None:
        self.size = size
        self.instructions = []
        self.variables = {}

    def set_instruction(self, instruction):
        self.instructions.append(instruction)

    def set_variable(self, variable_name: str, value: int):
        self.variables[variable_name] = value

    
