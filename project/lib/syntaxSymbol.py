from project.lib.nfa import NfaGraph, NfaEdge, NfaState, EndType
from project.lib.element import Element


class E:
    def __init__(self, nfa: NfaGraph):
        self.nfa = nfa


# Function: reduce E to E | E
def nfaOrCombine(E1: E, E2: E) -> E:
    endState = NfaState(
        edgeList=[]
    )

    newEdgeList = []
    newEdgeList.append(
        NfaEdge(
            driverChar="ep",
            nextState=E1.nfa.startState
        )
    )
    newEdgeList.append(
        NfaEdge(
            driverChar="ep",
            nextState=E2.nfa.startState
        )
    )

    startState = NfaState(
        edgeList=newEdgeList
    )

    E1.nfa.endState.edgeList.append(
        NfaEdge(
            driverChar="ep",
            nextState=endState
        )
    )

    E2.nfa.endState.edgeList.append(
        NfaEdge(
            driverChar="ep",
            nextState=endState
        )
    )

    newNfaGraph = NfaGraph(
        startState=startState,
        endState=endState,
        endStateType=EndType.INCLUDE,
        endStateClass=E1.nfa.endStateClass
    )

    return E(newNfaGraph)


# Function: reduce E to E & E
def nfaAndCombine(E1: E, E2: E) -> E:
    E1.nfa.endState.edgeList.append(
        NfaEdge(
            driverChar="ep",
            nextState=E2.nfa.startState
        )
    )

    return E(
        nfa=NfaGraph(
            startState=E1.nfa.startState,
            endState=E2.nfa.endState,
            endStateType=EndType.INCLUDE,
            endStateClass=E1.nfa.endStateClass
        )
    )


# Function: reduce E to (E)
def nfaBracketCombine(E1: E) -> E:
    return E1


# Function: reduce E to E#
def nfaPlusClosureCombine(E1: E) -> E:
    E1.nfa.endState.edgeList.append(
        NfaEdge(
            driverChar="ep",
            nextState=E1.nfa.startState
        )
    )

    return E1


# Function: reduce E to E@
def nfaClosureCombine(E1: E) -> E:
    E1.nfa.startState.edgeList.append(
        NfaEdge(
            driverChar="ep",
            nextState=E1.nfa.endState
        )
    )
    E1.nfa.endState.edgeList.append(
        NfaEdge(
            driverChar="ep",
            nextState=E1.nfa.startState
        )
    )

    return E1


# Function: reduce E to E?
def nfaZeroOneCombine(E1: E) -> E:
    E1.nfa.startState.edgeList.append(
        NfaEdge(
            driverChar="ep",
            nextState=E1.nfa.endState
        )
    )

    return E1


# Function: reduce E to id, create a simple nfa
def nfaNew(element: Element, reType: int) -> E:
    endState = NfaState(
        edgeList=[]
    )

    newEdgeList = []
    newEdgeList.append(
        NfaEdge(
            driverChar=element.name,
            nextState=endState
        )
    )

    startState = NfaState(
        edgeList=newEdgeList
    )

    newNfaGraph = NfaGraph(
        startState=startState,
        endState=endState,
        endStateType=EndType.INCLUDE,
        endStateClass=reType
    )
    newE = E(newNfaGraph)
    return newE
