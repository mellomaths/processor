from enum import Enum


class InstructionSet(Enum):
    LW = "LW"
    SW = "SW"
    ADD = "ADD"
    SUB = "SUB"
    AND = "AND"
    OR = "OR"
    BEQ = "BEQ"


class Instruction:

    def __init__(self, type: str, execution) -> None:
        self.type = type
        self.execution = execution
