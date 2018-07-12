def algo(n, k, answer):
    if n == 1:
        answer.append(k)
        return 0
    elif k < 2**(n-1):
        answer.append(0)
        return algo(n-1, k, answer)
    elif k >= 2**(n-1):
        answer.append(1)
        return algo(n-1, 2**n-1-k, answer)

def output(answer):
    for i in answer:
        print(i,end='')
    print()
    return 0

def main():
    answer = []
    str = input()
    str = str.split()
    n = int(str[0])
    k = int(str[1])
    algo(n, k, answer)
    output(answer)
    while 1 :
        answer = []
        interval = input()
        if interval == '-1':
            break
        else:
            str = input()
            str = str.split()
            n = int(str[0])
            k = int(str[1])
            algo(n, k, answer)
            output(answer)

main()
