def main():
    name = input()
    id = input()
    score = []
    total = 0
    for i in range(3):
        score.append(int(input()))
    for i in score:
        total = total + i
    average = total / 3
    print('Name:{}'.format(name))
    print('Id:{}'.format(id))
    print('Total:{}'.format(total))
    print('Average:{}'.format(int(average)))
main()
