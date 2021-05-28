from project.lib.nfa import NfaGraph, NfaState, NfaEdge,\
                            EndType, epsilonClosure, move


class DfaState:
    STATENUM = 0

    def __init__(
        self, edgeList: list, isEndState: bool,
        endStateClass: int, coreStateList: frozenset
    ):
        self.visited = 0
        self.isEndState = isEndState
        self.endStateClass = endStateClass  # 结束得到的类的类型，为LexcialType枚举类型
        self.stateId = DfaState.STATENUM  # 状态编号，为静态变量
        DfaState.STATENUM = DfaState.STATENUM + 1
        self.edgeList = edgeList  # 状态出边，为EdgeList类型
        self.coreStateList = coreStateList  # 状态的NFA核心项，用于查重


class DfaEdge:

    def __init__(self, driverChar: str, nextState: DfaState):
        self.driverChar = driverChar  # 驱动字符，只能为一个char字符
        self.nextState = nextState  # 跳转状态，为Dfa类型


class DfaGraph:

    def __init__(
        self, startState: DfaState,
        endStateList: set, endStateType: EndType, endStateClass: int
    ):
        self.startState = startState  # 起始状态，为DfaState类型
        self.endStateList = endStateList      # 结束状态，为DfaState类型
        self.endStateType = endStateType  # 结束状态类型，为EndType枚举类型
        self.endStateClass = endStateClass  # 结束得到的类的类型，为LexcialType枚举类型

    def __str__(self):
        returnStr = ""
        stateQueue = [self.startState]

        while len(stateQueue) != 0:
            nowState = stateQueue.pop()
            if nowState.visited == 0:
                for edge in nowState.edgeList:
                    if edge.nextState.isEndState:
                        returnStr = returnStr + "{} -> {} by {} end get {}\n".format(
                            nowState.stateId,
                            edge.nextState.stateId,
                            edge.driverChar,
                            edge.nextState.endStateClass
                        )
                    else:
                        returnStr = returnStr + "{} -> {} by {}\n".format(
                            nowState.stateId,
                            edge.nextState.stateId,
                            edge.driverChar
                        )
                    stateQueue.append(edge.nextState)
                nowState.visited = 1
        return returnStr


# Function: transform nfa graph to minimum dfa graph
def NfaToDfa(reNfaGraph: NfaGraph) -> DfaGraph:
    nowStateList = []
    startState = DfaState(
        isEndState=False,
        endStateClass=reNfaGraph.endStateClass,
        coreStateList={reNfaGraph.startState},
        edgeList=[]
    )

    nowStateList.append(startState)
    endStateList = []
    index = 0

    while index < len(nowStateList):
        eClosure, outEdgeList = epsilonClosure(nowStateList[index].coreStateList)
        for state in eClosure:
            if state.stateId == reNfaGraph.endState.stateId:
                nowStateList[index].isEndState = True
                endStateList.append(nowStateList[index])

        for outEdge in outEdgeList:
            arriveStateList = move(outEdgeList, driverChar=outEdge.driverChar)
            hasFlag = False
            for state in nowStateList:
                if state.coreStateList == arriveStateList:
                    hasFlag = True
                    print("Get a state {} which has appeared\n".format(state.stateId))
                    nowStateList[index].edgeList.append(
                        DfaEdge(
                            driverChar=outEdge.driverChar,
                            nextState=state
                        )
                    )

            if not hasFlag:
                newState = DfaState(
                    isEndState=False,
                    endStateClass=reNfaGraph.endStateClass,
                    coreStateList=arriveStateList,
                    edgeList=[]
                )
                nowStateList.append(newState)
                nowStateList[index].edgeList.append(
                    DfaEdge(
                        driverChar=outEdge.driverChar,
                        nextState=newState
                    )
                )
        index = index + 1

    reDfaGraph = DfaGraph(
        startState=startState,
        endStateList=endStateList,
        endStateType=EndType.INCLUDE,
        endStateClass=reNfaGraph.endStateClass
    )

    return reDfaGraph


# Function: merge dfa graphs to a whole dfa
def mergeDfaGraphs(reDfaGraphList: list) -> DfaGraph:
    # startState = DfaState(
    #     isEndState=False,
    #     endStateClass=RegularExpression.LexcialType[NONE],
    #     edgeList=[],
    #     coreStateList=frozenset()
    # )

    # for dfaGraph in reDfaGraphList:
    #     for another in reDfaGraphList:
    #         if dfaGraph is not another:
    #             for edge1 in dfaGraph.startState.edgeList:
    #                 for edge2 in another.startState.edgeList:
    #                     if edge1.driverChar == edge2.driverChar:

    pass


# Function: take nfa graph list and return the whole dfa graph
def DfaConstruct(reNfaGraphList: list) -> list:
    # Finished: transform every nfa graph to dfa graph
    reDfaGraphList = []
    for reNfaGraph in reNfaGraphList:
        reDfaGraphList.append(NfaToDfa(reNfaGraph=reNfaGraph))
    num = 0
    print("Print the DFA graphs: ")
    for reNfaGraph in reDfaGraphList:
        print("DFA graph {}".format(num))
        print(reNfaGraph)
        num = num + 1

    # return reDfaTotalGraph
    return reDfaGraphList
