import random

class AABB:
    def __init__(self):
        self.name = 'AABB'
        self.data = self.createNewGame()

    def getName(self):
        return self.name

    def output(self):
        if len(self.data) == 1:
            return self.data[0]
        else:
            print(self.data)
            return False

    def createNewGame(self):
        temp = []
        for i in range(0, 9999):
            tempStr = str(i)
            while len(tempStr) < 4 :
                tempStr = '0' + tempStr
            if self.checkSame(tempStr):
                pass
            else:
                temp.append(tempStr)
        return temp

    def checkSame(self, num):
        for i in range(0, 4):
            for j in range(i + 1, 4):
                if num[i] == num[j]:
                    return True
        return False

    def check(self, answer, guess, clue):
        answerList = []
        guessList = []
        clueList = [int(clue[0]), int(clue[2])]
        a = 0
        b = 0
        for i in answer:
            answerList.append(int(i))
        for i in guess:
            guessList.append(int(i))
        for i in range(0, 4):
            for j in range(0, 4):
                if guessList[i] == answerList[j]:
                    if i == j:
                        a = a + 1
                        break
                    else:
                        b = b + 1
                        break
                else:
                    pass
        if a == clueList[0] and b == clueList[1]:
            return True
        else:
            return False

    def getAnswer(self, inputStr):
        # print(data)
        if not len(self.data) == 1:
            temp = inputStr.split(',')
            popList = []
            for i in self.data:
                if i == 0:
                    pass
                else:
                    if self.check(i, temp[0], temp[1]):
                        pass
                    else:
                        popList.append(self.data.index(i))
            for i in reversed(popList):
                self.data.pop(i)
        print('計算中...')
