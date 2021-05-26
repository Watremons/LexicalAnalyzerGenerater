from project.lib.dfa import DfaState, DfaConstruct
from project.lib.nfa import NfaState
from project.lib.regularExpression import RegularExpression

from project.syntaxAnalysisTable import parseTextToSyntaxTable
from project.syntaxAnalysisLR import doLRSyntaxAnalysis, generateTestList
import os
import sys
sys.path.append("../")


# Function: get path of analysisTable.txt
def getTableFilePath():
    nowPath = os.path.dirname(__file__)

    dirPath = os.path.join(nowPath, "lib")
    if (os.path.isdir(dirPath)):
        actionListPath = os.path.join(dirPath, "actionList.txt")
        gotoListPath = os.path.join(dirPath, "gotoList.txt")

        if (os.path.isfile(actionListPath)):
            if (os.path.isfile(gotoListPath)):
                return actionListPath, gotoListPath
            else:
                print("The file \'../lib/gotoList.txt\' is not exist!")
                return None
        else:
            print("The file \'../lib/actionList.txt\' is not exist!")
            return None
    else:
        print("The dir \'../lib\' is not exist!")
        return None


# Function: do syntax analysis
def doSyntaxAnalysis(reList: list) -> str:
    actionTable = []
    gotoTable = []
    actionListPath, gotoListPath = getTableFilePath()
    actionListText = ""
    gotoListText = ""

    # Finished: get action table string and goto table string from file
    if actionListPath is not None:
        f = open(actionListPath, 'r', encoding='utf-8')
        actionListText = f.read()
        f.close()
    else:
        print("Can't get action table file!")
        return

    if gotoListText is not None:
        f = open(gotoListPath, 'r', encoding='utf-8')
        gotoListText = f.read()
        f.close()
    else:
        print("Can't get goto table file!")
        return

    # Finished: get action table and goto table
    actionTable, gotoTable = parseTextToSyntaxTable(actionListText, gotoListText)
    print("Print the action table:")
    for row in actionTable:
        for action in row:
            print(action, end=" ")
        print()
    print("Print the goto table:")
    for row in gotoTable:
        for goto in row:
            print(goto, end=" ")
        print()

    # Finished: get nfaGraphList of every regular expression
    reNfaGraphList = doLRSyntaxAnalysis(reList, actionTable, gotoTable)
    if (reNfaGraphList == "error"):
        print("Syntax Error: Please check your input")

    print("Print the NFA graphs: ")
    num = 0
    for reNfaGraph in reNfaGraphList:
        print("NFA graph {}".format(num))
        num = num + 1
        print(reNfaGraph)

    # # unfinished: parse nfa Graph to dfa graph and get total dfa
    reDfaTotalGraph = DfaConstruct(reNfaGraphList)
    # for reDfaGraph in reDfaTotalGraph:
    #     print(reDfaGraph)

    return


if __name__ == "__main__":
    reList = generateTestList()
    # reList.append(RegularExpression(,,,,))
    doSyntaxAnalysis(reList)
