class RType:

    def __init__(self, destination_register: int, first_operand_register: int, second_operand_register: int) -> None:
        self.destination_register = destination_register
        self.first_operand_register = first_operand_register
        self.second_operand_register = second_operand_register

