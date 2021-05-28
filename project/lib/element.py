from enum import Enum


# 定义元素类型
class ElementType(Enum):
    CHARACTER = 0  # 元素类型为输入字符
    VARIANT = 1  # 元素类型为正则表达式
    OPERATOR = 2  # 元素类型为运算符


class Element:
    ELEMENTID = 0

    def __init__(self, classType: ElementType, name: str, remark="Nothing"):
        self.elementId = Element.ELEMENTID  # 元素的序号，类型为int
        Element.ELEMENTID = Element.ELEMENTID + 1
        self.classType = classType  # 元素的类型，使用ElementType枚举，类型为输入字符
        self.name = name  # 元素的名称，输入字符或正则表达式名称或操作符
        self.remark = remark  # 元素备注

    def __str__(self):
        return "{}: {}  [type:{}]".format(self.elementId, self.name, self.classType)
