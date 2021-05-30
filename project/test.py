from project.lib.dfa import DfaGraph, DfaState, DfaEdge
from project.syntaxAnalysis import doSyntaxAnalysis
from project.lib.regularExpression import RegularExpression
from project.lexicalAnalysis import doLexicalAnalysis

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
def parseTextToLexeme(dfaGraph: DfaGraph, inputText: str) -> list:
    returnList = []
    typeDict = {v: k for k, v in RegularExpression.LexcialType.items()}
    print(typeDict)
    lexemeText = inputText.replace("\n", " ").replace("\t", " ")
    print(lexemeText)
    nowState = dfaGraph.startState
    lexeme = ""
    index = 0

    # Get one char a time and traverse the dfa
    while index < len(lexemeText):
        nowChar = lexemeText[index]
        hasNext = False
        anyDriverCharState = None

        # For a char, search for a edge and move to next state
        for edge in nowState.edgeList:
            # Set a anyDriverCharState to be picked if there is not a match edge
            if edge.driverChar == "^":
                anyDriverCharState = edge.nextState
            if edge.driverChar == nowChar:
                nowState = edge.nextState
                lexeme = lexeme + nowChar
                hasNext = True
                break

        # Can't move, check whether nowState is an endState
        # Or nowState has an anyDriverCharState to move
        if not hasNext:
            # if nowState has an anyDriverCharState to move
            if anyDriverCharState is not None:
                nowState = anyDriverCharState
                lexeme = lexeme + nowChar
            else:
                # Check whether nowState is the start state
                if nowState.stateId != dfaGraph.startState.stateId:
                    # Check whether nowState is an endState
                    if nowState.isEndState:
                        returnList.append({lexeme: typeDict[nowState.endStateClass]})
                    else:
                        returnList.append({lexeme: typeDict[0]})
                    nowState = dfaGraph.startState
                    lexeme = ""
                    index = index - 1
                # if so, clear lexeme
                else:
                    lexeme = ""
        # Get next char
        index = index + 1

    # Check whether nowState is the start state
    if nowState.stateId != dfaGraph.startState.stateId:
        # Check whether nowState is an endState
        if nowState.isEndState:
            returnList.append({lexeme: typeDict[nowState.endStateClass]})
        else:
            returnList.append({lexeme: typeDict[0]})
        nowState = dfaGraph.startState
        lexeme = ""

    # if so, clear lexeme
    else:
        lexeme = ""

    return returnList


# Function: do test by real code
def testDfaGraphByFile(dfaGraph: DfaGraph, inputFileName: str) -> list:
    filePath = getInputFilePath(inputFileName)
    inputText = ""
    if filePath is not None:
        f = open(filePath, 'r', encoding='utf-8')
        inputText = f.read()
        f.close()
    else:
        print("Can't get input file!")
        return

    resultList = parseTextToLexeme(dfaGraph, inputText)
    return resultList


if __name__ == "__main__":
    reList = doLexicalAnalysis()

    dfaGraph = doSyntaxAnalysis(reList)
    if dfaGraph == "error":
        print("Error: the input regular expressions have syntax error")
        exit(1)
    print("\n")
    # Finished: do test and get return
    # inputFileName = input("Lexer has already generated.\nPlease input the code filename:")
    inputFileName = "sample.tny"
    lexemeList = testDfaGraphByFile(dfaGraph=dfaGraph, inputFileName=inputFileName)
    for lexeme in lexemeList:
        print(lexeme)
    exit(0)
