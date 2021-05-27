from project.lib.dfa import DfaGraph, DfaState, DfaEdge
from project.syntaxAnalysis import doSyntaxAnalysis
from project.lib.regularExpression import RegularExpression

import os


# Function: get path of analysisTable.txt
def getInputFilePath(filename):
    nowPath = os.path.dirname(__file__)

    dirPath = nowPath
    if (os.path.isdir(dirPath)):
        inputFilePath = os.path.join(dirPath, filename)

        if (os.path.isfile(inputFilePath)):
            return inputFilePath
        else:
            print("The file {} is not exist!".format(inputFilePath))
            return None
    else:
        print("The dir {} is not exist!".format(nowPath))
        return None


# Function: do lexcial analysis
def parseTextToLexeme(dfaGraphList: list, inputText: str) -> list:
    pass


# Function: do test by real code
def testDfaGraphByFile(dfaGraphList: list, inputFileName: str) -> list:
    filePath = getInputFilePath(inputFileName)
    inputText = ""
    if filePath is not None:
        f = open(filePath, 'r', encoding='utf-8')
        inputText = f.read()
        f.close()
    else:
        print("Can't get input file!")
        return

    resultList = parseTextToLexeme(dfaGraphList, inputText)
    return resultList


if __name__ == "__main__":
    reList = doLexicalAnalysis()

    dfaGraphList = doSyntaxAnalysis(reList)

    # # Unfinished: do test and get return
    # inputFileName = input("Lexer has already generated.\nPlease input the code filename:")
    inputFileName = "sample.tny"
    lexemeList = testDfaGraphByFile(dfaGraphList=dfaGraphList, inputFilename=inputFileName)
    for lexeme in lexemeList:
        print(lexeme)
    x = RegularExpression.LexcialType["NONE"]
    print(x)
