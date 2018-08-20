def algo(p, n):
    if p < n:
        return 0
    elif n == 1:
        if p <= 6:
            return 1
        else:
            return 0
    else:
        return algo(p-6,n-1) + algo(p-5,n-1) + algo(p-4,n-1) + algo(p-3,n-1) + algo(p-2,n-1) + algo(p-1,n-1)

def main():
    inputStr = input().split(' ')
    temp = int(inputStr[0])
    num = int(inputStr[1])
    max = temp * 6
    answer = 0
    for i in range(num, max+1):
        # print('answer: ', answer)
        # print('i: ', i)
        answer += algo(i, temp)
    print(answer)
    print(6**temp)

main()
