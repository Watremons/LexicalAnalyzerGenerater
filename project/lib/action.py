from enum import Enum


class ActionType(Enum):
    ERROR = 0
    SHIFT = 1
    REDUCE = 2
    ACCEPT = 3


class ReduceType(Enum):
    DO_NONE = 0
    DO_OR = 1
    DO_AND = 2
    DO_BRACKET = 3
    DO_PLUS_CLOSURE = 4
    DO_CLOSURE = 5
    DO_ZERO_ONE = 6
    DO_ID = 7


class Action:

    def __init__(self, actionType: ActionType, shiftNum: int, reduceNum: ReduceType):
        self.actionType = actionType
        self.shiftNum = shiftNum
        self.reduceNum = reduceNum

    def __str__(self):
        if (self.actionType == ActionType.SHIFT):
            return ("s" + str(self.shiftNum)).ljust(3, " ")
        elif (self.actionType == ActionType.REDUCE):
            return ("r" + str(int(self.reduceNum.value))).ljust(3, " ")
        elif (self.actionType == ActionType.ACCEPT):
            return "acc"
        else:
            return "   "


if __name__ == "__main__":
    action = Action(
        actionType=ActionType.SHIFT,
        shiftNum=3,
        reduceNum=ReduceType.DO_NONE
    )

    if action.actionType == ActionType.SHIFT:
        print("Yes")
    else:
        print("No")
