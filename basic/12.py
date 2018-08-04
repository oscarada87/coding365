def main():
    temp = int(input())
    if temp != 10:
        temp2 = int(input())
        answer = temp + temp2
    else:
        answer = 10
    temp = int(input())
    if temp != 10:
        temp2 = int(input())
        temp3 = 0
    else:
        temp2 = 0
        temp3 = int(input())
    answer += temp + temp2 + temp3
    print(answer)

main()
