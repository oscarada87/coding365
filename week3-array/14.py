def checkSame(num):
    for i in range(0, 4):
        for j in range(i + 1, 4):
            if num[i] == num[j]:
                return True
    return False

def createNewGame():
    temp = []
    for i in range(0, 9999):
        tempStr = str(i)
        while len(tempStr) < 4 :
            tempStr = '0' + tempStr
        if checkSame(tempStr):
            pass
        else:
            temp.append(tempStr)
    return temp

def check(answer, guess, clue):
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

def main():
    data = createNewGame()
    # print(data)
    while not len(data) == 1:
        temp = input().split(',')
        popList = []
        for i in data:
            if i == 0:
                pass
            else:
                if check(i, temp[0], temp[1]):
                    pass
                else:
                    popList.append(data.index(i))
        for i in reversed(popList):
            data.pop(i)
    print(data[0])

main()
