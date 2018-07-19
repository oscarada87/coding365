import abc
import sys

class Part(abc.ABC):
    @abc.abstractmethod
    def getName(self):
        return NotImplemented
    @abc.abstractmethod
    def getPrice(self):
        return NotImplemented
    @abc.abstractmethod
    def info(self):
        return NotImplemented

class CPU(Part):
    def getName(self):
        return 'CPU'
    def getPrice(self):
        return 20
    def info(self):
        print('name: ', 'CPU')
        print('cost: ', 20)

class HD(Part):
    def getName(self):
        return 'HD'
    def getPrice(self):
        return 35
    def info(self):
        print('name: ', 'HD')
        print('cost: ', 35)

class RAM(Part):
    def getName(self):
        return 'RAM'
    def getPrice(self):
        return 50
    def info(self):
        print('name: ', 'RAM')
        print('cost: ', 50)

class Singleton(object):
    _instance = None
    def __new__(cls, *args, **kw):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kw)
            return cls._instance
        else:
            print('ERROR!!!!')
            print('Class can\'t announce twice')
            sys.exit()
            # cls._instance = super(Singleton, cls).__new__(cls, *args, **kw)



class register(Singleton):
    def __init__(self):
        self.partList = []
    def addPart(self, part):
        self.partList.append(part)
    def total(self):
        amount = 0
        for i in self.partList:
            amount = amount + i.getPrice()
        print('total: ', amount)

reg = register()
reg2 = register()
reg.addPart(CPU())
reg.addPart(HD())
reg.addPart(CPU())
reg.addPart(RAM())
reg.addPart(CPU())
reg.total()
