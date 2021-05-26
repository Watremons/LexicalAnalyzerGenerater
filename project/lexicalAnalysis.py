from posixpath import lexists
from project.lib.element import Element, ElementType
from project.lib.dfa import DfaState, DfaConstruct
from project.lib.nfa import NfaState
from project.lib.regularExpression import LexcialType, RegularExpression

import os
import sys
sys.path.append("../")


def getTableFilePath():
    nowPath = os.path.dirname(__file__)

    dirPath = os.path.join(nowPath, "lib")
    if (os.path.isdir(dirPath)):
        actionListPath = os.path.join(dirPath, "re1.txt")
        gotoListPath = os.path.join(dirPath, "gotoList1.txt")

        if (os.path.isfile(actionListPath)):
            if (os.path.isfile(gotoListPath)):
                return actionListPath, gotoListPath
            else:
                print("The file \'../lib/gotoList1.txt\' is not exist!")
                return None
        else:
            print("The file \'../lib/re1.txt\' is not exist!")
            return None
    else:
        print("The dir \'../lib\' is not exist!")
        return None


def getExpression(reList):
    ansList = []
    classType = ElementType(0)
    name = ""
    remark = ""
    for nowElement in reList:
        if nowElement == "digit" or nowElement == "fullDigit" or nowElement == "letter" or nowElement == "if" or nowElement == "then" or nowElement == "else" or nowElement == "end" or nowElement == "repeat" or nowElement == "until" or nowElement == "read" or nowElement == "write":
            classType = ElementType(1)
        elif str.isdigit(nowElement) or str.isupper(nowElement) or str.islower(
                nowElement):
            classType = ElementType(0)
        else:
            classType = ElementType(2)
        name = nowElement
        el = Element(classType, name, remark)
        ansList.append(el)
    return ansList

def prn_obj(obj): 
  print(obj.__dict__)

def doSyntaxAnalysis():
    actionListPath, gotoListPath = getTableFilePath()
    f = open(actionListPath, 'r', encoding='utf-8')

    regularExpressionList = []
    for line in f.readlines():
        print(line)
        tLine = line.replace("\n", "")
        lineTable = []
        reList = []
        expressionList = []

        lineTable = tLine.split('~')
        head = lineTable[0].strip()
        reList = lineTable[1].split(" ")
        print(reList)

        headElement = Element(ElementType(1), head, "")
        expressionList = getExpression(reList)
        lexcialclass = LexcialType(0)
        if head == "digit" or head == "fullDigit" or head == "int":
            lexcialclass = LexcialType(1)
        elif head == "id":
            lexcialclass = LexcialType(0)
        else:
            lexcialclass = LexcialType(2)

        re=RegularExpression(headElement,expressionList,lexcialclass,"")
        regularExpressionList.append(re)
        # print(expressionList[0])
        # print(head+"hhh")

        # RegularExpression re(W)
    for obj in regularExpressionList:
        print("head:")
        print(prn_obj(obj.headElement))
        print("expression:")
        for exobj in obj.expression:
            prn_obj(exobj)
        print(obj.lexcialClass)

    # print(prn_obj(regularExpressionList[0]))
    return regularExpressionList


if __name__ == "__main__":
    # reList.append(RegularExpression(,,,,))
    doSyntaxAnalysis()
