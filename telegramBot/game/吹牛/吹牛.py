import abc
import random

class Player:
    def __init__(self, number):
        self.data = ()
        self.number = number
    def getNumber(self):
        return self.number
    def getData(self):
        return self.data
    def setData(self, data):
        self.data = data

class Game:
    def __init__(self):
        self.member = []
        self.i = 0
        self.time = 0
    def Join(self,player):
        self.member.append(player)
    @abc.abstractmethod
    def StartGame():
        return Notimplemented

class DiceGame(Game):
    def StartData(self):
        for x in self.member:
            data_temp=[]
            for _ in range(6):
                data_temp.append(random.randint(1,6))
            data_temp.sort()
            x.setData(tuple(data_temp))

    def StartGame(self):
        stander=[]
        while True:
            inpu=input("input your choise:").split(",")
            if self.ReviewInput(inpu)==True:
                if inpu[1]=="抓":
                    self.WinOrLose(self.i,inpu,stander)
                    break
                elif inpu[0]==self.member[self.i].getNumber():
                    if self.time==0:
                        stander=[int(inpu[1]),int(inpu[2])]
                        self.time=1
                        self.i=self.i+1
                    else:
                        if(int(inpu[1])<stander[0]) or (int(inpu[2])<stander[1]) or (int(inpu[1])==stander[0] and int(inpu[2])==stander[1]) :
                            print("error now is ",stander)
                        elif int(inpu[1])>6 or int(inpu[2])>6:
                            print("your input outoff range")
                        else:
                            stander[0]=int(inpu[1])
                            stander[1]=int(inpu[2])
                            if self.i==len(self.member)-1:
                                self.i=0
                            else:
                                self.i=self.i+1
                else :
                    print("error input please try again")
                if stander[0]==6 and stander[1]==6:
                    inpu=input("input:").split(",")
                    self.WinOrLose(i,inpu,stander)
                    break

    def WinOrLose(self,i,inpu,stander):
        yrdata=self.member[self.i-1].getData()
        num1=yrdata.count(1)
        numinpu=yrdata.count(stander[1])
        print(yrdata,num1,numinpu)
        if numinpu+num1<int(stander[0]):
            print("player {} is the winner".format(inpu[0]))
        else:
            print("player {} you fail,player {} you win\nplayer {} dice is {}".format(inpu[0],self.member[self.i-1].Name(),self.member[self.i-1].Name(),yrdata))
    def ReviewInput(self,inpu):
        if len(inpu)!=2 and len(inpu) != 3:
            print("your input was error \nplease try again")
        elif inpu[0] not in temp:
            print("you are not player")
        elif inpu[1]=="抓":
            if self.time == 0:
                print("you have input value\nplease try again")
            elif inpu[0] == self.member[self.i-1].Name():
                print("you can't use 抓 this function")
            else: return True
        elif inpu[1].isdigit()==False or inpu[2].isdigit()==False:
            return "you have invade input\nplease try again"
        elif int(inpu[1])<1 or int(inpu[2])<1:
            return "you can't play like this"
        elif int(inpu[1])>6 or int(inpu[2])>6:
            return "your input outoff range"
        else:
            return True
Dice=DiceGame()
temp=[]
while(True):
    inpu=input("input:").split("/")
    if inpu[0] == "start":
        break
    elif inpu[1] == "join":
        temp.append(inpu[0])
        inpu[0]=Player(inpu[0])
        Dice.Join(inpu[0])
    else:
        print("error inpu")
Dice.StartData()
Dice.StartGame()
