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

def splitTree(number, preorder, inorder, nodeList, father, flag = 0):
    if len(inorder) == 0:
        return 0
    index = inorder.find(preorder[number])
    if index == -1:
        splitTree(number + 1, preorder, inorder, nodeList, father, flag)
        return 0
    leftList = inorder[:index]
    # print('leftList:', leftList)
    rightList = inorder[index + 1:]
    # print('rightList:', rightList)
    nodeList.append(node(preorder[number]))
    if flag == 0:
        pass
    elif flag == 1:
        father.setLeft(nodeList[-1])
    elif flag == 2:
        father.setRight(nodeList[-1])
    splitTree(number + 1, preorder, leftList, nodeList, nodeList[-1], 1)
    splitTree(number + 1, preorder, rightList, nodeList, nodeList[-1], 2)

def main():
    nodeList = []
    preorder = 'ABDECF'
    inorder = 'DBEAFC'
    splitTree(preorder, inorder, nodeList)
    for i in nodeList:
        print(i.getNumber())

main()
