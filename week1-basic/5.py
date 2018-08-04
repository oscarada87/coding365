import math

def average(data):
    total = 0
    for i in data:
        total = total + i
    return total / 5

def var(data, avr):
    answer = 0
    for i in data:
        answer = answer + abs(i - avr) ** 2
    return answer / 5

def main():
    str = input().split(' ')
    data = []
    for i in str:
        data.append(int(i))
    avr = average(data)
    var1 = var(data, avr)
    std = var1 ** 0.5
    avr = '%.3f' % avr
    var1 = '%.3f' % var1
    std = '%.3f' % std
    print(avr[:-1])
    print(var1[:-1])
    print(std[:-1])

main()
