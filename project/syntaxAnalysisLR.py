from project.lib.regularExpression import RegularExpression
from project.lib.element import Element, ElementType
from project.lib.action import Action, ActionType, ReduceType
from project.lib.syntaxSymbol import \
    nfaOrCombine, nfaAndCombine, nfaBracketCombine,\
    nfaPlusClosureCombine, nfaClosureCombine, nfaZeroOneCombine, nfaNew


def doLRSyntaxAnalysis(reList: list, actionTable: list, gotoTable: list) -> list:
    reNfaGraphList = []
    # traverse all regular expressions
    for re in reList:
        print(re.headElement)
        # Symbol table is reList
        reType = re.lexcialClass
        stateStack = [0]
        symbolStack = []
        nowState = -1
        index = 0
        length = len(re.expression)
        # start LR syntax analysis
        while (len(stateStack) != 0):
            if index > length:
                print("Syntax Error: the re is end before get accept state")
                return "error"
            nowState = stateStack[-1]
            nowElement = re.expression[index]
            # get a corresponding action
            nowAction = getAction(nowState, nowElement, actionTable)

            # do action
            if nowAction.actionType == ActionType.SHIFT:
                stateStack.append(nowAction.shiftNum)
                symbolStack.append(nowElement)
                index = index + 1
            elif nowAction.actionType == ActionType.REDUCE:
                if (nowAction.reduceNum == ReduceType.DO_OR):
                    # get 3 object
                    E2 = symbolStack.pop()
                    symbolStack.pop()
                    E1 = symbolStack.pop()

                    # do or combine and push result
                    symbolStack.append(nfaOrCombine(E1, E2))

                    # pop 3 state
                    stateStack.pop()
                    stateStack.pop()
                    stateStack.pop()
                elif (nowAction.reduceNum == ReduceType.DO_AND):
                    # get 3 object
                    E2 = symbolStack.pop()
                    symbolStack.pop()
                    E1 = symbolStack.pop()

                    # do and combine and push result
                    symbolStack.append(nfaAndCombine(E1, E2))

                    # pop 3 state
                    stateStack.pop()
                    stateStack.pop()
                    stateStack.pop()
                elif (nowAction.reduceNum == ReduceType.DO_BRACKET):
                    # get 3 object
                    symbolStack.pop()
                    E1 = symbolStack.pop()
                    symbolStack.pop()

                    # do bracket combine and push result
                    symbolStack.append(nfaBracketCombine(E1))

                    # pop 3 state
                    stateStack.pop()
                    stateStack.pop()
                    stateStack.pop()
                elif (nowAction.reduceNum == ReduceType.DO_PLUS_CLOSURE):
                    # get 2 object
                    symbolStack.pop()
                    E1 = symbolStack.pop()

                    # do plus closure combine and push result
                    symbolStack.append(nfaPlusClosureCombine(E1))

                    # pop 2 state
                    stateStack.pop()
                    stateStack.pop()
                elif (nowAction.reduceNum == ReduceType.DO_CLOSURE):
                    # get 2 object
                    symbolStack.pop()
                    E1 = symbolStack.pop()

                    # do closure combine and push result
                    symbolStack.append(nfaClosureCombine(E1))

                    # pop 2 state
                    stateStack.pop()
                    stateStack.pop()
                elif (nowAction.reduceNum == ReduceType.DO_ZERO_ONE):
                    # get 2 object
                    symbolStack.pop()
                    E1 = symbolStack.pop()

                    # do zero one combine and push result
                    symbolStack.append(nfaZeroOneCombine(E1))

                    # pop 2 state
                    stateStack.pop()
                    stateStack.pop()
                elif (nowAction.reduceNum == ReduceType.DO_ID):
                    # get 1 object
                    topOne = symbolStack.pop()
                    if not isinstance(topOne, Element):
                        print("Syntax Error: can't get continuous unterminal symbol")
                        return "error"
                    # do zero one combine and push result
                    symbolStack.append(nfaNew(topOne, reType))

                    # pop 1 state
                    stateStack.pop()
                else:
                    print("Unknown Error: get a unknown type of reduce action")
                    return "error"

                backState = stateStack[-1]  # get backState
                stateStack.append(gotoTable[backState][0])  # push goto state
            elif nowAction.actionType == ActionType.ACCEPT:
                break
            elif nowAction.actionType == ActionType.ERROR:
                print("Syntax Error: get a wrong action")
                print("Now state: {}\tNow element: {}".format(nowState, nowElement))
                return "error"
            else:
                print("Unknown Error: get a unknown type of action")
                return "error"

        # Handle exceptions
        if index != length-1:
            print("Syntax Error: get accept state but the re is not end")
            return "error"
        if len(symbolStack) != 1:
            print("Syntax Error: get accept state but the symbols is not reduced")
            return "error"
        reNfaGraphList.append(symbolStack.pop().nfa)

    return reNfaGraphList


def getAction(nowState, nowElement, actionTable):
    if (nowElement.classType == ElementType.CHARACTER):
        return actionTable[nowState][0]
    elif (nowElement.classType == ElementType.OPERATOR):
        if (nowElement.name == "|"):
            return actionTable[nowState][1]
        elif (nowElement.name == "&"):
            return actionTable[nowState][2]
        elif (nowElement.name == "]"):
            return actionTable[nowState][3]
        elif (nowElement.name == "["):
            return actionTable[nowState][4]
        elif (nowElement.name == "$"):
            return actionTable[nowState][5]
        elif (nowElement.name == "#"):
            return actionTable[nowState][6]
        elif (nowElement.name == "@"):
            return actionTable[nowState][7]
        elif (nowElement.name == "?"):
            return actionTable[nowState][8]
        else:
            return Action(
                actionType=ActionType.ERROR,
                shiftNum=-1,
                reduceNum=ReduceType.DO_NONE
            )
    else:
        return Action(
            actionType=ActionType.ERROR,
            shiftNum=-1,
            reduceNum=ReduceType.DO_NONE
        )


def generateTestList():
    expression = []
    expression.append(
        Element(
            classType=ElementType.CHARACTER,
            name="i",
        )
    )
    expression.append(
        Element(
            classType=ElementType.OPERATOR,
            name="&",
        )
    )
    expression.append(
        Element(
            classType=ElementType.CHARACTER,
            name="f",
        )
    )
    expression.append(
        Element(
            classType=ElementType.OPERATOR,
            name="|",
        )
    )
    expression.append(
        Element(
            classType=ElementType.OPERATOR,
            name="[",
        )
    )
    expression.append(
        Element(
            classType=ElementType.CHARACTER,
            name="e",
        )
    )
    expression.append(
        Element(
            classType=ElementType.OPERATOR,
            name="&",
        )
    )
    expression.append(
        Element(
            classType=ElementType.CHARACTER,
            name="l",
        )
    )
    expression.append(
        Element(
            classType=ElementType.OPERATOR,
            name="]",
        )
    )
    expression.append(
        Element(
            classType=ElementType.OPERATOR,
            name="#",
        )
    )
    expression.append(
        Element(
            classType=ElementType.OPERATOR,
            name="&",
        )
    )
    expression.append(
        Element(
            classType=ElementType.CHARACTER,
            name="s",
        )
    )
    expression.append(
        Element(
            classType=ElementType.OPERATOR,
            name="&",
        )
    )
    expression.append(
        Element(
            classType=ElementType.CHARACTER,
            name="e",
        )
    )
    expression.append(
        Element(
            classType=ElementType.OPERATOR,
            name="$",
        )
    )

    re = RegularExpression(
        headElement=Element(
            ElementType.VARIANT,
            "testLex",
            "用于测试的元素"
        ),
        expression=expression,
        lexcialClass=RegularExpression.LexcialType["RESERVED"],
        remark="测试用例"
    )

    print(re)

    reList = []
    reList.append(re)

    return reList


if __name__ == "__main__":
    print("do a valid import")
