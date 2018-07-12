class node:
    def __init__(self, number):
        self.number = number
        self.father = None
        self.left = None
        self.right = None
    def setRight(self, right):
        self.right = right
    def setLeft(self, left):
        self.left = left
    def setFather(self, father):
        self.father = father
    def getRight(self):
        return self.right
    def getLeft(self):
        return self.left
    def getFather(self):
        return self.father
    def getNumber(self):
        return self.number
    def isroot(self):
        if self.father == None:
            return True
        else:
            return False

def insertNode(nodeList):
    number = int(input())
    if len(nodeList) == 0:
        rootNode = node(number)
        nodeList.append(rootNode)
    else:
        rootNode = nodeList[0]
        temp = rootNode
        target = node(number)
        while 1:
            if number > temp.getNumber():
                if temp.getRight() == None:
                    temp.setRight(target)
                    target.setFather(temp)
                    break
                else:
                    temp = temp.getRight()
            elif number <= temp.getNumber():
                if temp.getLeft() == None:
                    temp.setLeft(target)
                    target.setFather(temp)
                    break
                else:
                    temp = temp.getLeft()

def inorderPrint(rootNode):
    if(rootNode == None):
        return 0
    inorderPrint(rootNode.getLeft())
    print(rootNode.getNumber(),end=' ')
    inorderPrint(rootNode.getRight())

def main():
    nodeList = []
    while 1:
        str = input()
        if str == 'e':
            break
        elif str == 'p':
            try:
                inorderPrint(nodeList[0])
                print()
            except IndexError:
                print('null')
        elif str == 'i':
            insertNode(nodeList)

main()
