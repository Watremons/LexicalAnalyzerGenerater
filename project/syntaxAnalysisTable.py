from lib.action import ActionType, ReduceType, Action


# Function: parse element string to action
def parseElementToAction(element: str):
    if element == "null":
        return Action(
            actionType=ActionType.ERROR,
            shiftNum=0,
            reduceNum=ReduceType.DO_NONE
        )
    elif element[0] == 's':
        return Action(
            actionType=ActionType.SHIFT,
            shiftNum=int(element[1:]),
            reduceNum=ReduceType.DO_NONE
        )
    elif element[0] == 'r':
        return Action(
            actionType=ActionType.REDUCE,
            shiftNum=-1,
            reduceNum=ReduceType(int(element[1:]))
        )
    elif element == "acc":
        return Action(
            actionType=ActionType.ACCEPT,
            shiftNum=-1,
            reduceNum=ReduceType.DO_NONE
        )
    else:
        return False


# Function: get action table and goto table
def parseTextToSyntaxTable(actionListText: str, gotoListText: str):
    actionStrList = actionListText.split("\n")
    gotoStrList = gotoListText.split("\n")

    actionTable = []
    for row in actionStrList:
        actionList = []
        elementList = row.split(',')
        for element in elementList:
            action = parseElementToAction(element)
            if action is not False:
                actionList.append(action)
        actionTable.append(actionList)

    gotoTable = []
    for row in gotoStrList:
        gotoList = []
        elementList = row.split(',')
        for element in elementList:
            gotoList.append(int(element))
        gotoTable.append(gotoList)

    return actionTable, gotoTable
