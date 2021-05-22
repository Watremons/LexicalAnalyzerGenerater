from regularExpression import LexcialType


class Lexeme:

    def __init__(self, elementOrOp, Lexemetype: LexcialType):
        self.elementOrOp = elementOrOp
        self.Lexemetype = Lexemetype
