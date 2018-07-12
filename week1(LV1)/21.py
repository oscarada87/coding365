def main():
    str = input()
    count = -1
    str = str.split(' ')
    N = int(str[0])
    M = int(str[1])
    K = int(str[2])
    people = []
    for j in range(1,N+1):
        people.append(j)
    for i in range(0,K):
        count = count + M
        if count >= len(people):
            count = count - len(people)
        print(people[count],end=' ')
        people.pop(count)
        count = count - 1
    if count >= len(people):
        count = count - len(people)
    try:
        print (people[count+1],end=' ')
    except IndexError:
        print (people[count],end=' ')
main()
