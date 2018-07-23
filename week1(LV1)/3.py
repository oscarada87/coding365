def check1(str):
    index = str.find('x')
    str = str[:index+1]
    if len(str) == 1:
        return 1
    else:
        return 0
def inputProcess(p):
    data = []
    p = p.split(' ')
    # print(p)
    # 常數項
    if p[-1].find('x') == -1:
        if p[-2] == '-':
            if check1(p[-1]):
                const = -1
            else:
                const = -int(p[-1])
        else:
            if check1(p[-1]):
                const = 1
            else:
                const = int(p[-1])
        p.pop()
        p.pop()
        data.append((const, 0))
    # 一次項
    if p[-1].find('^') == -1:
        if p[-2] == '-':
            if check2(p[-1]):
                first = -1
            else:
                first = -int(p[-1])
        else:
            if check1(p[-1]):
                first = 1
            else:
                first = int(p[-1])
        p.pop()
        p.pop()
        data.append((first, 1))
    # 其他次方
    # print(p)
    length = int((len(p) + 1) / 2)
    for i in range(1, length, 2):
        index = p[i+1].find('^')
        power = int(p[i+1][index + 1:])
        index = p[i+1].find('x')
        if p[i] == '-':
            if check1(p[i]):
                co = -1
            else:
                co = -int(p[i+1][:index])
        else:
            if check1(p[i]):
                co = 1
            else:
                co = int(p[i+1][:index])
        data.append((co, power))
    # 最高次方
    if len(p) != 0:
        index = p[0].find('^')
        power = int(p[0][index + 1:])
        index = p[0].find('x')
        temp = p[0][:index]
        if temp == '-':
            co = -1
        elif temp == '':
            co = 1
        else:
            co = int(temp)
        data.append((co, power))
    return data

def main():
    method = input()
    polynomial1 = inputProcess(input())
    polynomial2 = inputProcess(input())
    print(polynomial1)
    print(polynomial2)

main()
