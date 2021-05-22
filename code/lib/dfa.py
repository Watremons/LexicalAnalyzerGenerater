from enum import Enum


# 定义结束状态的类型
class EndType(Enum):
    EXCLUDE = 0  # 匹配状态，但不包含当前字符
    INCLUDE = 1  # 匹配状态，但包含当前字符


class Dfa:

    def __init__(self, element, edgeList):
        self.element = element  # 状态元素，为Element类型
        self.edgeList = edgeList  # 状态出边，为EdgeList类型


class DfaGraph:

    def __init__(self, startState, endState, endStateType, endStateClass):
        self.startState = startState  # 起始状态，为Dfa类型
        self.endState = endState      # 结束状态，为Dfa类型
        self.endStateType = endStateType  # 结束状态类型，为EndType枚举类型
        self.endStateClass = endStateClass  # 结束得到的类的类型，为LexcialType枚举类型


class DfaEdge:

    def __init__(self, driverChar, nextState):
        self.driverChar = driverChar  # 驱动字符，为一个char字符，或是为空
        self.nextState = nextState  # 跳转状态，为Dfa类型
