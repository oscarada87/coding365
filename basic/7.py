def main():
    temp = int(input())
    total = A(temp)
    temp = int(input())
    total = total + B(temp)
    temp = int(input())
    total = total + C(temp)
    print(int(total))

def A(num):
    if num <= 10:
        return 380 * num
    elif num <= 20:
        return 380 * num * 0.9
    elif num <= 30:
        return 380 * num * 0.85
    elif num >= 31:
        return 380 * num * 0.8

def B(num):
    if num <= 10:
        return 1200 * num
    elif num <= 20:
        return 1200 * num * 0.95
    elif num <= 30:
        return 1200 * num * 0.85
    elif num >= 31:
        return 1200 * num * 0.8

def C(num):
    if num <= 10:
        return 180 * num
    elif num <= 20:
        return 180 * num * 0.85
    elif num <= 30:
        return 180 * num * 0.8
    elif num >= 31:
        return 180 * num * 0.7
main()
