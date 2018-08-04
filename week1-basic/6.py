import math

def main():
    a = float(input())
    b = float(input())
    c = float(input())
    check = b*b - 4*a*c
    if check >= 0:
        T = math.sqrt(check)
        temp = -b + T
        temp = temp / (2*a)
        temp = '%.2f' % temp
        temp = str(temp)[:-1]
        temp2 = -b - T
        temp2 = temp2 / (2*a)
        temp2 = '%.2f' % temp2
        temp2 = str(temp2)[:-1]
        print(temp)
        print(temp2)
    elif check < 0:
        T2 = abs(check)
        abst = abs(math.sqrt(T2) / (2*a))
        abst = '%.2f' % abst
        abst = str(abst)[:-1]
        re = -b / (2*a)
        re = '%.2f' % re
        re = str(re)[:-1]
        if a > 0:
            print('{}+{}i'.format(re, abst))
            print('{}-{}i'.format(re, abst))
        else:
            print('{}-{}i'.format(re, abst))
            print('{}+{}i'.format(re, abst))

main()
