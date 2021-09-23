from enum import Enum


class ALUOperation(Enum):
    AND = "0000"
    OR = "0001"
    ADD = "0010"
    SUB = "0110"
    SLT = "0111"
    NOR = "1100"


class ALU:

    def __init__(self) -> None:
        pass

    def execute(self, operation: str, operand1: int, operand2: int) -> int:
        if operation == ALUOperation.ADD:
            return operand1 + operand2


