import abc

class DrinkBuilder:
    def __init__(self, name):
        self.name = name
    @abc.abstractmethod
    def brew(self):
        return NotImplemented
    @abc.abstractmethod
    def flavor(self):
        return NotImplemented
    @abc.abstractmethod
    def mix(self):
        return NotImplemented

    def howToMake(self):
        print('第一步: ',end = '')
        self.brew()
        print('第二步: ',end = '')
        self.flavor()
        print('第三步: ',end = '')
        self.mix()
    def getName(self):
        return self.name

class MilkTea(DrinkBuilder):
    def __init__(self):
        super(MilkTea, self).__init__('milktea')
    def brew(self):
        print('泡紅茶')
    def flavor(self):
        print('泡鮮奶')
    def mix(self):
        print('灑上少許巧克力粉')

class Coffee(DrinkBuilder):
    def __init__(self):
        super(Coffee, self).__init__('coffee')
    def brew(self):
        print('研磨')
    def flavor(self):
        print('加入奶精')
    def mix(self):
        print('灑上少許肉桂粉')

a = MilkTea()
print(a.getName())
a.howToMake()
b = Coffee()
print(b.getName())
b.howToMake()
