from lib.dfa import DfaState, DfaConstruct
from lib.nfa import NfaState
from lib.regularExpression import RegularExpression

from syntaxAnalysisTable import parseElementToAction, parseTextToSyntaxTable
from syntaxAnalysisLR import doLRSyntaxAnalysis
import os


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

    actionTable, gotoTable = parseTextToSyntaxTable(actionListText, gotoListText)
    # Finished: get action table and gotoT table

    reNfaGraphList = doLRSyntaxAnalysis(reList, actionTable, gotoTable)
    # unfinished: get nfaGraphList of every regular expression

    reDfaTotalGraph = DfaConstruct(reNfaGraphList)
    # unfinished: parse nfa Graph to dfa graph and get total dfa

    for reDfaGraph in reDfaTotalGraph:
        print(reDfaGraph)

    return


if __name__ == "__main__":
    reList = []
    # reList.append(RegularExpression(,,,,))
    doSyntaxAnalysis(reList)
