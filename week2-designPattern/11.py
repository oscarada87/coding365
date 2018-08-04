import abc

class Stock(abc.ABC):
    def __init__(self, name):
        self.name = name
        self.memberList = []

    def attach(self, member):
        for i in self.memberList:
            if i.getName() == member.getName():
                print('Member was already exist!!')
                return 0
        self.memberList.append(member)
        return 0

    def detach(self, member):
        for i in self.memberList:
            if i.getName() == member.getName():
                self.memberList.remove(i)
                return 0
        print('Member didn\'t exist!!')
        return 0

    def notify(self):
        print('{}\'s price is now {}'.format(self.name, self.getPrice()))
        for i in self.memberList:
            i.update()
        return 0

class Asus(Stock):
    def __init__(self, price):
        super(Asus, self).__init__('Asus')
        self.price = price

    def getPrice(self):
        return self.price

class Member(abc.ABC):
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def getName(self):
        return self.name

    def getLevel(self):
        return self.level

    @abc.abstractmethod
    def update(self):
        return NotImplemented

class NormalMember(Member):
    def __init__(self, name):
        super(NormalMember, self).__init__(name, 1)

    def update(self):
        print('--Normal member-- {} recieve a new message!!'.format(self.name))

class VIP1Member(Member):
    def __init__(self, name):
        super(VIP1Member, self).__init__(name, 2)

    def update(self):
        print('--VIP1 member-- {} recieve a new message!!'.format(self.name))

A = Asus(100)
Tom = NormalMember('Tom')
Ben = VIP1Member('Ben')
A.attach(Tom)
A.attach(Ben)
A.notify()
