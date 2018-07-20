def inputProcess(a):
    data = []
    for i in a:
        if len(i) == 2:
            temp = (int(i[0]),int(i[1]))
        else:
            temp = (int(i[:2]), int(i[2]))
        data.append(temp)
    return data

def pair(data):
    if data[0][0] == data[1][0]:
        return 1
    elif data[1][0] == data[2][0]:
        return 1
    elif data[2][0] == data[3][0]:
        return 1
    elif data[3][0] == data[4][0]:
        return 1
    else:
        return 0
def twoPair(data):
    if data[0][0] == data[1][0] and data[2][0] == data[3][0]:
        return 1
    elif data[1][0] == data[2][0] and data[2][0] == data[3][0]:
        return 1
    else:
        return 0

def threeOfAKind(data):
    if data[0][0] == data[1][0] == data[2][0]:
        return 1
    elif data[1][0] == data[2][0] == data[3][0]:
        return 1
    elif data[2][0] == data[3][0] == data[4][0]:
        return 1
    else:
        return 0
def fullHouse(data):
    if data[0][0] == data[1][0] == data[2][0] and data[3][0] == data[4][0]:
        return 1
    elif data[0][0] == data[1][0] and data[2][0] == data[3][0] == data[4][0]:
        return 1
    else:
        return 0

def fourOfAKind(data):
    if data[0][0] == data[1][0] == data[2][0] == data[3][0]:
        return 1
    elif data[1][0] == data[2][0] == data[3][0] == data[4][0]:
        return 1
    else:
        return 0

def flush(data):
    if data[0][1] == data[1][1] == data[2][1] == data[3][1] == data[4][1]:
        return 1
    else:
        return 0

def straight(data):
    if data[4][0] == 13 and data[0][0] + 4 == data[1][0] + 3 == data[2][0] + 2 == data[3][0] + 1:
        return 1
    elif data[0][0] + 4 == data[1][0] + 3 == data[2][0] + 2 == data[3][0] + 1 == data[4][0]:
        return 1
    else:
        return 0

def judge(data):
    if straight(data) and flush(data):
        print('7')
        return 0
    elif straight(data):
        print('6')
        return 0
    elif fourOfAKind(data):
        print('5')
        return 0
    elif fullHouse(data):
        print('4')
        return 0
    elif threeOfAKind(data):
        print('3')
        return 0
    elif twoPair(data):
        print('2')
        return 0
    elif pair(data):
        print('1')
        return 0
    else:
        print('0')
        return 0

def main():
    a = [i for i in input().split(' ')]
    data = inputProcess(a)
    data.sort()
    # print(data)
    judge(data)

main()
