class node:
    def __init__(self, number, top = None):
        self.number = number
        self.top = top
        self.downList = []
    def settop (self, top):
        self.top = top
    def setdown (self, down):
        self.downList.append(down)
    def getnumber (self):
        return self.number
    def gettop (self):
        return self.top
    def getdown (self):
        return self.downList
    def isroot (self):
        if self.top == None:
            return True
        else:
            return False

def getDistanceToRoot(nodeList, a):
    A = nodeList[a]
    path = [A.getnumber()]
    temp = A
    while temp.isroot() == False:
        temp = temp.gettop()
        path.append(temp.getnumber())
    return path

def getDistance(pathA, pathB):
    # remove same
    tempA = pathA.copy()
    tempB = pathB.copy()
    for i in pathA:
        for j in pathB:
            if i == j:
                tempA.remove(i)
                tempB.remove(i)
    return len(tempA) + len(tempB)

def main():
    # input stage
    nodeList = []
    disToRoot = []
    total = int(input())
    for i in range(total):
        nodeList.append(node(i))
    for i in range(total - 1):
        temp = input()
        temp = temp.split(' ')
        nodeList[int(temp[0])].setdown(nodeList[int(temp[1])])
        nodeList[int(temp[1])].settop(nodeList[int(temp[0])])
    for i in range(total):
        disToRoot.append(getDistanceToRoot(nodeList, i))
    # for i in range(total):
    #     print(disToRoot[i])
    for i in range(total):
        for j in range(i+1,total):
            print("{}-{}-{}".format(i, j, getDistance(disToRoot[i],disToRoot[j])))
    # print(getDistance(disToRoot[4],disToRoot[6]))
    # for i in range(total):
    #     if nodeList[i].isroot == False:
    #         print(nodeList[i].gettop().getnumber())
    #     else:
    #         print('root')

main()








# a = node(0)
# b = node(1,0)
# a.setdown(b)
# print(a.getdown().getnumber())
