def algo(n):
    if n == 1:
        return 1
    elif n == 0:
        return 1
    elif n == 2:
        return 2
    else:
        return algo(n-1) + algo(n-2) + algo(n-3)
def main():
    number = int(input())
    print(algo(number))

main()
