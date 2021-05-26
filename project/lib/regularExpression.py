from enum import Enum
from project.lib.element import Element, ElementType


# 定义正则表达式词法类型
class LexcialType(Enum):
    NONE = -1  # 错位类型
    IDENTIFIER = 0  # 正则表达式词法类型为变量
    NUMERIC = 1  # 正则表达式词法类型为数字
    RESERVED = 2  # 正则表达式词法类型为保留字


class RegularExpression:

    def __init__(self, headElement: Element, expression: list, lexcialClass: LexcialType, remark="Nothing"):
        self.headElement = headElement  # 元素头部元素，为Element类型元素
        self.expression = expression  # 正则表达式的主体部分, 用element类型的list表示
        self.lexcialClass = lexcialClass  # 正则表达式的类型，为LexcialType
        self.remark = remark  # 正则表达式注释

    def __str__(self):
        returnStr = ""
        returnStr = returnStr + self.headElement.name
        returnStr = returnStr + " -> "
        for element in self.expression:
            returnStr = returnStr + element.name
        returnStr = returnStr + "  [type:{}]".format(self.lexcialClass)
        return returnStr


if __name__ == "__main__":
    r = RegularExpression(
        Element(1, ElementType.CHARACTOR, "0", "测试"),
        "0",
        LexcialType.IDENTIFIER,
        "测试表达式子",
    )

    print(r)
