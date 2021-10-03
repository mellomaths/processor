from enum import Enum


class InstructionSet(Enum):
    LW = "LW"
    SW = "SW"
    ADD = "ADD"
    SUB = "SUB"
    AND = "AND"
    OR = "OR"
    BEQ = "BEQ"
