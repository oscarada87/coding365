def check(data):
    count = 0
    if data[0][1] > data[1][0]:
        temp = [data[0][0], data[1][1]]
        data.append(temp)
        data.pop(0)
        data.pop(0)
        data.sort()
        # print(data)
        if data[0][1] > data[1][0]:
            temp = [data[0][0], data[1][1]]
            data.append(temp)
            data.pop(0)
            data.pop(0)
            data.sort()
        else:
            pass
    else:
        if data[1][1] > data[2][0]:
            temp = [data[1][0], data[2][1]]
            data.append(temp)
            data.pop(1)
            data.pop(1)
            data.sort()
        else:
            pass


def main():
    data = []
    for i in range(3):
        temp = [int(input()), int(input())]
        temp.sort()
        data.append(temp)
    data.sort()
    check(data)
    answer = 0
    for i in data:
        answer += i[1] - i[0]
    print(answer)
main()
