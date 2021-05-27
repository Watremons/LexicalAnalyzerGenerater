from enum import Enum


# 定义结束状态的类型
class EndType(Enum):
    EXCLUDE = 0  # 匹配状态，但不包含当前字符
    INCLUDE = 1  # 匹配状态，但包含当前字符


class NfaState:
    STATENUM = 0

    def __init__(self, edgeList: list):
        self.visited = 0
        self.stateId = NfaState.STATENUM
        NfaState.STATENUM = NfaState.STATENUM + 1
        self.edgeList = edgeList  # 状态出边，为EdgeList类型


class NfaEdge:

    def __init__(self, driverChar: str, nextState: NfaState):
        self.driverChar = driverChar  # 驱动字符，为一个char字符,空为"ep"
        self.nextState = nextState  # 跳转目标状态，为Dfa类型


class NfaGraph:

    def __init__(self, startState: NfaState, endState: NfaState, endStateType: EndType, endStateClass: int):
        self.startState = startState  # 起始状态，为Dfa类型
        self.endState = endState      # 结束状态，为Dfa类型
        self.endStateType = endStateType  # 结束状态类型，为EndType枚举类型
        self.endStateClass = endStateClass  # 结束得到的类的类型，为LexcialType枚举类型

    def __str__(self):
        returnStr = ""
        stateQueue = [self.startState]

        while len(stateQueue) != 0:
            nowState = stateQueue.pop()
            if nowState.visited == 0:
                for edge in nowState.edgeList:
                    returnStr = returnStr + "{} -> {} by {}\n".format(
                        nowState.stateId,
                        edge.nextState.stateId,
                        edge.driverChar
                    )
                    stateQueue.append(edge.nextState)
                nowState.visited = 1
        return returnStr


# Function: get epsilon closure of states
def epsilonClosure(startStateList: set):
    eClosure = set()
    outEdgeList = set()
    for nowState in startStateList:
        eClosure.add(nowState)

    while True:
        eClosureCopy = eClosure.copy()
        for state in eClosureCopy:
            # print(state.stateId)
            for edge in state.edgeList:
                if edge.driverChar == "ep":
                    eClosure.add(edge.nextState)
                else:
                    outEdgeList.add(edge)
        if len(eClosure) == len(eClosureCopy):
            break
    return eClosure, outEdgeList


# Function: get move set of closure and char
def move(outEdgeList: set, driverChar: str) -> frozenset:
    arriveStateList = set()
    for edge in outEdgeList:
        if edge.driverChar == driverChar:
            arriveStateList.add(edge.nextState)
    return frozenset(arriveStateList)
