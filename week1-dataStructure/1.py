def stackAdd(data,new):
    if len(data) >= 5:
        print("FULL")
        return 1
    data.append(new)
    return 0

def circularAdd(data,new):
    if len(data) > 3:
        print("FULL")
        return 1
    data.append(new)
    return 0

def stackDelete(data):
    if len(data) == 0:
        print("EMPTY")
        return 1
    data.pop()
    return 0

def circularDelete(data):
    if len(data) == 0:
        print("EMPTY")
        return 1
    data.pop(0)
    return 0

def output(data):
    for i in data:
        print(i, end=' ')
    return 1

def main():
    data = []
    choice = input()
    if choice == '1':
        while 1:
            str = input()
            str = str.split(' ')
            if str[0] == '1':
                if stackAdd(data,str[1]):
                    break
            elif str[0] == '2':
                if stackDelete(data):
                    break
            elif str[0] == '3':
                output(data)
                break
            else:
                break
    elif choice == '2':
        while 1:
            str = input()
            str = str.split(' ')
            if str[0] == '1':
                if circularAdd(data,str[1]):
                    break
            elif str[0] == '2':
                if circularDelete(data):
                    break
            elif str[0] == '3':
                output(data)
                break
            else:
                break
    return 0
main()
