from project.lib.element import Element, ElementType


class RegularExpression:
    # 定义正则表达式词法类型
    LexcialType = {
        "NONE": 0,
        "IDENTIFIER": 2,
        "NUMERIC": 3,
        "RESERVED": 1
    }

    def __init__(self, headElement: Element, expression: list, lexcialClass: int, remark="Nothing"):
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
        RegularExpression.LexcialType["IDENTIFIER"],
        "测试表达式子",
    )

    print(r)
