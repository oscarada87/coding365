def check(row, num):
    total = 0
    indexNum = None
    temp = [num]
    for i in row:
        total = int(i) + total
        if i == '0':
            indexNum = row.index(i)
    # print(total, num, indexNum)
    if indexNum == None:
        return 0
    else:
        temp.append(indexNum)
        temp.append(45 - total)
        return temp


def main():
    sudo = []
    answer = []
    for i in range(0, 9):
        sudo.append(input())
    for i in range(0, 9):
        if check(sudo[i], i) == 0:
            pass
        else:
            answer.append(check(sudo[i], i))
    for i in answer:
        for j in i:
            print(j, ' ',end='')
        print()

main()
