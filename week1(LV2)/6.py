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

def splitTree(preorder, inorder, nodeList, root = None, count = 0):
    try:
        devide = inorder.index(preorder[count])
    except ValueError:
        count = count + 1
        if count >= len(preorder):
            return 0

        print('count:',count)
        splitTree(preorder, inorder, nodeList, nodeList[-1], count)
    leftList = inorder[:devide]
    print('leftList:', leftList)
    rightList = inorder[devide + 1:]
    print('rightList:', rightList)
    nodeList.append(node(preorder[count]))
    if root == None:
        pass
    else:
        nodeList[-1].setFather(root)
        if root.getLeft() == None:
            root.setLeft(nodeList[-1])
        else:
            root.setRight(nodeList[-1])
    count = count + 1
    if count >= len(preorder):
        return 0
    splitTree(preorder, leftList, nodeList, nodeList[-1], count)
    splitTree(preorder, rightList, nodeList, nodeList[-1], count)

def main():
    nodeList = []
    preorder = 'ABDECF'
    inorder = 'DBEAFC'
    splitTree(preorder, inorder,nodeList)
    for i in nodeList:
        print(i.getNumber())

main()
