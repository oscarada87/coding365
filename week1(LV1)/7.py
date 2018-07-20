class triangle:
    def __init__(self, pointList):
        self.pointList = pointList
        self.rayList = []
    def calculate(self):
        for i in range(3):
            for j in range(i, 3):
                temp = self.pointList[i][0] - self.pointList[j][0]
                temp2 = self.pointList[i][1] - self.pointList[j][1]
            rayList.append((temp, temp2))
