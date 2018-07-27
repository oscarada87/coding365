import abc

class Student(abc.ABC):
    def __init__(self, name, midterm, finalExam, assignment, usual):
        self.name = name
        self.midterm = midterm
        self.finalExam = finalExam
        self.assignment = assignment
        self.usual = usual
    # 建立抽象function- finalScore
    @abc.abstractmethod
    def finalScore(self):
        return NotImplemented

# 去年學生
class Student107(Student):
    def __init__(self, name, midterm, finalExam, assignment, usual):
        # 呼叫父類別的init函式
        super(Student107, self).__init__(name, midterm, finalExam, assignment, usual)
    # 實作finalScore
    def finalScore(self):
        score = self.midterm * 0.25 + self.finalExam * 0.35 + self.assignment * 0.3 + self.usual * 0.1
        print('{}\'s final score: {}'.format(self.name, score))
        return score
# Ben 100 100 100 100    學期總成績應為: 100
# XioMing 50 75 32 85    學期總成績應為: 56.85
# Peter 46 89 32 90      學期總成績應為: 61.25
# 測試

Ben = Student107('Ben', 100, 100, 100, 100)
XioMing = Student107('XioMing', 50, 75, 32, 85)
Peter = Student107('Peter', 46, 89, 32, 90)
print('107 Students:')
Ben.finalScore()
XioMing.finalScore()
Peter.finalScore()

# 今年學生
class Student108(Student):
    def __init__(self, name, midterm, finalExam, assignment, usual, addPoint):
        # 呼叫父類別的init函式
        super(Student108, self).__init__(name, midterm, finalExam, assignment, usual)
        # 新增 加分 這個新的屬性
        self.addPoint = addPoint
    # 實作finalScore
    def finalScore(self):
        score = self.midterm * 0.3 + self.finalExam * 0.3 + self.assignment * 0.2 + self.usual * 0.2 + self.addPoint
        print('{}\'s final score: {}'.format(self.name, score))
        return score
# Brian 100 100 100 100 3 學期總成績應為: 103
# XioMing 50 75 32 85 5   學期總成績應為: 65.9
# Apple 46 89 32 90 0     學期總成績應為: 64.9
# 測試
Brian = Student108('Brian', 100, 100, 100, 100, 3)
XioMing = Student108('XioMing', 50, 75, 32, 85, 5)
Apple = Student108('Apple', 46, 89, 32, 90, 0)
print('108 Students:')
Brian.finalScore()
XioMing.finalScore()
Apple.finalScore()
