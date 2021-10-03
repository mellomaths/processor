from processor.instructions.set.r_type import RType


class Sub(RType):

    def __init__(self, destination_register: int, first_operand_register: int, second_operand_register: int) -> None:
        super().__init__(destination_register, first_operand_register, second_operand_register)
