class node():
    def __init__(self, name, father = None, left = None, right = None):
        self.name = name
        self.father = father
        self.left = left
        self.right = right
    def getName(self):
        return self.name
    def getFather(self):
        return self.father
    def getLeft(self):
        return self.left
    def getRight(self):
        return self.right
    def setFather(self, father):
        self.father = father
    def setLeft(self, left):
        self.left = left
    def setRight(self, right):
        self.right = right
    def isRoot(self):
        if self.father == None:
            return True
        else:
            return False
# flag = 0-----------root
# flag = 1-----------left
# flag = 2-----------right
def devideP(number, data, inorder, nodeList, flag = 0, father = None):
    if len(inorder) == 0:
        return 0
    # if father != None:
    #     print(inorder, father.getName())
    index = inorder.find(data[number])
    if index == -1 :
        return  devideP(number + 1, data, inorder, nodeList, flag, father)
    else:
        pass
    leftList = inorder[:index]
    rightList = inorder[index + 1:]
    if flag == 0:
        nodeList.append(node(data[number]))
    elif flag == 1:
        nodeList.append(node(data[number]))
        father.setLeft(nodeList[-1])
    elif flag == 2:
        nodeList.append(node(data[number]))
        father.setRight(nodeList[-1])
    target = nodeList[-1]
    devideP(number + 1, data, leftList, nodeList, 1, target)
    devideP(number + 1, data, rightList, nodeList, 2, target)

def devideO(number, data, inorder, nodeList, flag = 0, father = None):
    if len(inorder) == 0:
        return 0
    if number < 0:
        return 0
    # if father != None:
    #     print(inorder, father.getName())
    index = inorder.find(data[number])
    if index == -1 :
        return  devideO(number - 1, data, inorder, nodeList, flag, father)
    else:
        pass
    leftList = inorder[:index]
    rightList = inorder[index + 1:]
    if flag == 0:
        nodeList.append(node(data[number]))
    elif flag == 1:
        nodeList.append(node(data[number]))
        father.setLeft(nodeList[-1])
    elif flag == 2:
        nodeList.append(node(data[number]))
        father.setRight(nodeList[-1])
    target = nodeList[-1]
    devideO(number - 1, data, leftList, nodeList, 1, target)
    devideO(number - 1, data, rightList, nodeList, 2, target)

def output(root):
    thisLevel = [root]
    while len(thisLevel) != 0:
        nextLevel = list()
        for n in thisLevel:
            print (n.getName(), end='')
            if n.getLeft() != None:
                nextLevel.append(n.getLeft())
            if n.getRight() != None:
                nextLevel.append(n.getRight())
        thisLevel = nextLevel


def main():
    nodeList = []
    typeA = input()
    dataA = input()
    typeB = input()
    dataB = input()
    if typeA == 'P':
        devideP(0, dataA, dataB, nodeList)
    elif typeB == 'P':
        devideP(0, dataB, dataA, nodeList)
    elif typeA =='O':
        number = len(dataA) - 1
        devideO(number, dataA, dataB, nodeList)
    elif typeB == 'O':
        number = len(dataB) - 1
        devideO(number, dataB, dataA, nodeList)
    output(nodeList[0])
    # for i in nodeList:
    #     left = i.getLeft()
    #     right = i.getRight()
    #     if left == None:
    #         if right == None:
    #             print(i.getName(), '-', 'None', '-', 'None')
    #         else:
    #             print(i.getName(), '-', 'None', '-', i.getRight().getName())
    #     else:
    #         if right == None:
    #             print(i.getName(), '-', i.getLeft().getName(), '-', 'None')
    #         else:
    #             print(i.getName(), '-', i.getLeft().getName(), '-', i.getRight().getName())



main()
# ABCDEFGHI
# BCAEDGHFI
