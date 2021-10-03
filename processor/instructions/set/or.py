from processor.instructions.set.r_type import RType


class Or(RType):

    def __init__(self, destination_register: int, register_operand1: int, register_operand2: int) -> None:
        super().__init__(destination_register, register_operand1, register_operand2)
