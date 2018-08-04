import math

def main():
    a = int(input())
    b = int(input())
    c = int(input())
    temp = -b + math.sqrt(b*b - 4*a*c)
    temp = temp / (2*a)
    temp2 = -b - math.sqrt(b*b - 4*a*c)
    temp2 = temp2 / (2*a)
    print('%.1f' % temp)
    print('%.1f' % temp2)

main()
