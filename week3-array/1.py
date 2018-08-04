def printList(a, b):
    print('A:[', end='')
    for i in a:
        print(i, ',', sep='', end='')
    print(']B:[', end='')
    for i in b:
        print(i, ',', sep='', end='')
    print(']')

def delete(a, number):
    try:
        temp = a.index(number)
    except ValueError:
        return 0
    a.pop(temp)

def union(a, b):   #聯集
    setA = set(a)
    setB = set(b)
    unionSet = setA | setB
    tempList = []
    for i in a:
        if i in unionSet:
            tempList.append(i)
    for i in b:
        if i in unionSet and not i in a:
            tempList.append(i)
    print('[', end='')
    for i in tempList:
        print(i, ',', sep='', end='')
    print(']')

def intersect(a, b):  #交集
    setA = set(a)
    setB = set(b)
    intersectSet = setA & setB
    tempList = []
    for i in a:
        if i in intersectSet:
            tempList.append(i)
    print('[', end='')
    for i in tempList:
        print(i, ',', sep='', end='')
    print(']')

def isSubset(a, b):
    setA = set(a)
    setB = set(b)
    if setA <= setB:
        print(1)
    else:
        print(0)

def main():
    a = []
    b = []
    while 1:
        str = input()
        str = str.split(' ')
        if str[0] == '0':
            break
        elif str[0] == '1':
            a.clear()
            printList(a, b)
        elif str[0] == '2':
            b.clear()
            printList(a, b)
        elif str[0] == '3':
            try:
                a.index(int(str[1]))
            except ValueError:
                a.append(int(str[1]))
            printList(a, b)
        elif str[0] == '4':
            try:
                b.index(int(str[1]))
            except ValueError:
                b.append(int(str[1]))
            printList(a, b)
        elif str[0] == '5':
            delete(a, int(str[1]))
            printList(a, b)
        elif str[0] == '6':
            delete(b, int(str[1]))
            printList(a, b)
        elif str[0] == '7':
            union(a, b)
        elif str[0] == '8':
            intersect(a, b)
        elif str[0] == '9':
            isSubset(a, b)

main()
