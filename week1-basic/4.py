def main():
    str = input().split(' ')
    data = []
    for i in str:
        data.append(int(i))
    data.sort()
    if data[0] + data[1] <= data[2]:
        print(1)
        return 0
    elif data[0] == data[1] == data[2]:
        print(2)
        return 0
    elif data[0] == data[1] or data[1] == data[2]:
        print(3)
        return 0
    else:
        print(4)
        return 0

main()
