
class Circle:
    def __init__(self, rad):
        self.rad = rad

    def getP(self):
        print(2 * 4 * self.rad)
        return 2 * 4 * self.rad

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def getP(self):
        print(self.width * 2 + self.height * 2)
        return self.width * 2 + self.height * 2

class Square:
    def __init__(self, board):
        self.board = board

    def getP(self):
        print(self.board * 4)
        return self.board * 4

class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def getP(self):
        print(self.a + self.b + self.c)
        return self.a + self.b + self.c

def main():
    temp = int(input())
    data = []
    answer = 0
    for i in range(temp):
        str = input().split(' ')
        if str[0] == 'C':
            data.append(Circle(int(str[1])))
        elif str[0] == 'R':
            data.append(Rectangle(int(str[1]),int(str[2])))
        elif str[0] == 'S':
            data.append(Square(int(str[1])))
        elif str[0] == 'T':
            data.append(Triangle(int(str[1]),int(str[2]),int(str[3])))
    for i in data:
        answer = answer + i.getP()

    print(answer)
main()
