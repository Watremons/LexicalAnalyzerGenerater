from project.lib.element import Element, ElementType


if __name__ == "__main__":
    newSet = set()
    element = Element(
        classType=ElementType.CHARACTOR,
        name="1"
    )
    newSet.add(element)
    newSet.add(Element(
        classType=ElementType.CHARACTOR,
        name="1"
    ))
    newSet.add(Element(
        classType=ElementType.CHARACTOR,
        name="2"
    ))
    newSet.add(1)
    newSet.add(111)

    num = 0
    newSetCopy = newSet.copy()
    for element in newSetCopy:
        print(element)
        newSet.add(num)

    sameValues = newSet & newSetCopy
    print(len(sameValues))
