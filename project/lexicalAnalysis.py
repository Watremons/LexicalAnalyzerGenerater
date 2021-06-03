from project.lib.element import Element, ElementType
from project.lib.regularExpression import RegularExpression

import os
import sys
sys.path.append("../")


def getTableFilePath():
    nowPath = os.path.dirname(__file__)

    if (os.path.isdir(nowPath)):
        actionListPath = os.path.join(nowPath, "re1.txt")

        if (os.path.isfile(actionListPath)):
            return actionListPath
        else:
            print("The file \'../re1.txt\' is not exist!")
            return None
    else:
        print("The dir \'..\' is not exist!")
        return None


def getExpression(reList):
    ansList = []
    classType = ElementType(0)
    name = ""
    remark = ""
    for nowElement in reList:
        if nowElement ==" ":
            continue
        # print("now:"+nowElement)
        if nowElement == "|" or nowElement == "[" or nowElement == "]" or nowElement == "&" or nowElement == "@" or nowElement == "#" or nowElement == "?":
            classType = ElementType(2)
        else:
            classType = ElementType(0)
        name = nowElement
        el = Element(classType, name, remark)
        ansList.append(el)
    el = Element(ElementType(2), '$', "")
    ansList.append(el)
    return ansList


def prn_obj(obj):
    print(obj.__dict__)


def doLexicalAnalysis():
    actionListPath = getTableFilePath()
    f = open(actionListPath, 'r', encoding='utf-8')

    cnt = 0
    regularExpressionList = []
    lexcialclass = RegularExpression.LexcialType["NONE"]
    flag = True

    for line in f.readlines():
        print(line)

        lineTable = []
        cnt += 1
        tLine = line.replace("\n", "")

        if cnt % 2 == 0:
            if flag is False:
                continue
            reList = []
            expressionList = []

            lineTable = tLine.split('~')
            head = lineTable[0].strip()
            # reList = lineTable[1].split(" ")
            # del(lineTable[1])
            # print(reList)

            headElement = Element(ElementType(1), head, "")
            expressionList = getExpression(lineTable[1])

            re = RegularExpression(headElement, expressionList, lexcialclass,
                                   "")
            regularExpressionList.append(re)

            cnt = 0
        else:
            flag = True
            lineTable = tLine.split(':')
            tName = lineTable[0].upper()
            myDict = RegularExpression.LexcialType
            if myDict.get(tName, "sb") == 0:
                if myDict[tName] != lineTable[1]:
                    print("废物，你TM给楠总滚")
                    flag = False
                    continue
                else:
                    lexcialclass = RegularExpression.LexcialType[tName]
            else:
                myDict[tName] = int(lineTable[1])
                lexcialclass = RegularExpression.LexcialType[tName]
            # print(myDict.get("NONE","sb"))
            # print(myDict)
            print(lexcialclass)

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
    doLexicalAnalysis()
