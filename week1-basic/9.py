def check(data):
    temp = data[0] * data[0]
    temp2 = data[1] * data[1]
    temp3 = data[2] * data[2]

    if data[0] + data[1] <= data[2]:
        print('Not Triangle')
        return 0
    elif temp + temp2 == temp3:
        print('Right Triangle')
        return 1
    elif temp + temp2 < temp3:
        print('Obtuse Triangle')
        return 2
    else:
        print('Acute Triangle')
        return 3


def main():
    str = input().split(' ')
    data = []
    for i in str:
        data.append(int(i))
    data.sort()
    check(data)

main()
