class Course:
    def __init__(self, name):
        self.name = name
        self.time = []
        self.allow = True

    def add(self, str):
        self.time.append(str)

    def getAllow(self):
        return self.allow
    def getTime(self):
        return self.time
    def getName(self):
        return self.name

def check(A, B):
    data = []
    for i in A.getTime():
        for j in B.getTime():
            if i == j:
                temp = A.getName() + ',' + B.getName() + ',' + i
                data.append(temp)
            else:
                pass
    return data

def allow(str):
    if int(str[0]) > 5 or int(str[0]) < 1 :
        return 0
    elif int(str[1]) > 8 or int(str[1]) < 1:
        return 0
    else:
        return 1

def main():
    data = []
    for i in range(3):
        temp = Course(input())
        times = int(input())
        for i in range(times):
            str = input()
            if allow(str) == 0:
                print(-1)
                return 0
            else:
                temp.add(str)
        data.append(temp)
    conflict = []
    conflict.extend(check(data[0],data[1]))
    conflict.extend(check(data[0],data[2]))
    conflict.extend(check(data[1],data[2]))
    if len(conflict) == 0:
        print('correct')
    else:
        for i in conflict:
            print(i)
main()
