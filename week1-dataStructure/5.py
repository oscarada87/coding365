class people():
    def __init__(self, name, cata):
        self.name = name
        self.preferList = []
        self.done = 0
        self.cata = cata
        self.partner = None
    def addPrefer(self, str):
        self.preferList.append(str)
    def getname(self):
        return self.name
    def getprefer(self):
        return self.preferList
    def getcata(self):
        return self.cata
    # def isdone(self):
    #     return self.done
    # def setdone(self):
    #     self.done = 1
    def setPartner(self, partner):
        self.partner = partner
    def getpartner(self):
        return self.partner

def checkPrefer(studentList, number, teacherList):
    tempList = [[] for i in range(5)]
    for i in studentList:
        if i.getpartner() == None:
            if i.getprefer()[number] == 'A' and teacherList[0].getpartner() == None:
                tempList[0].append(i)
            elif i.getprefer()[number] == 'B' and teacherList[1].getpartner() == None:
                tempList[1].append(i)
            elif i.getprefer()[number] == 'C' and teacherList[2].getpartner() == None:
                tempList[2].append(i)
            elif i.getprefer()[number] == 'D' and teacherList[3].getpartner() == None:
                tempList[3].append(i)
            elif i.getprefer()[number] == 'E' and teacherList[4].getpartner() == None:
                tempList[4].append(i)
        else:
            pass
    for index, i in enumerate(tempList):
        if len(i) == 1:
            if index == 0:
                i[0].setPartner(teacherList[0].getname())
                teacherList[0].setPartner(i[0].getname())
            elif index == 1:
                i[0].setPartner(teacherList[1].getname())
                teacherList[1].setPartner(i[0].getname())
            elif index == 2:
                i[0].setPartner(teacherList[2].getname())
                teacherList[2].setPartner(i[0].getname())
            elif index == 3:
                i[0].setPartner(teacherList[3].getname())
                teacherList[3].setPartner(i[0].getname())
            elif index == 4:
                i[0].setPartner(teacherList[-1].getname())
                teacherList[-1].setPartner(i[0].getname())
        elif len(i) > 1:
            for target in teacherList[index].getprefer():
                end = 0
                for test in i:
                    if target == test.getname():
                        test.setPartner(teacherList[index].getname())
                        teacherList[index].setPartner(test.getname())
                        end = 1
                        break
                    else:
                        pass
                if end == 1:
                    break
        else:
            pass
    # for i in tempList:
    #     for j in i:
    #         print(j.getname())
    # print(tempList)
def main():
    studentList = []
    teacherList = []
    first = input()
    first = first.split(',')
    total = len(first)
    studentList.append(people(chr(90-total+1),'student'))
    for j in range(total):
        studentList[0].addPrefer(first[j])
    for i in range(1, total):
        temp = input()
        temp = temp.split(',')
        studentList.append(people(chr(90+i-total+1),'student'))
        for j in range(total):
            studentList[i].addPrefer(temp[j])
    for i in range(total):
        temp = input()
        temp = temp.split(',')
        teacherList.append(people(chr(65+i),'teacher'))
        for j in range(total):
            teacherList[i].addPrefer(temp[j])
    for i in range(total):
        checkPrefer(studentList, i, teacherList)
    for i in range(total):
        print("{}->{}".format(studentList[i].getname(),studentList[i].getpartner()))
    # for i in range(4):
    #     print(studentList[i].getpartner())
    # debugggggggggggggggggggggggg
    # for i in range(4):
    #     print(studentList[i].getname())
    #     print(studentList[i].getprefer())
    # debugggggggggggggggggggggggg
main()
