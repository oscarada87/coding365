import abc

# 抽象類別---水果
class Fruit:
    def __init__(self, type):
        self.type = type
    @abc.abstractmethod
    def plant(self):
        return NotImplemented
    @abc.abstractmethod
    def grow(self):
        return NotImplemented
    @abc.abstractmethod
    def harvest(self):
        return NotImplemented

class Grape(Fruit):
    def __init__(self, seed):
        self.seed = seed
        super(Grape, self).__init__('Grape')

    def plant(self):
        print(self.type, ' planting!!!')
    def grow(self):
        print(self.type, ' growing!!!')
    def harvest(self):
        print(self.type, ' harvesting!!!')

class Strawberry(Fruit):
    def __init__(self):
        super(Strawberry, self).__init__('Strawberry')

    def plant(self):
        print(self.type, ' planting!!!')
    def grow(self):
        print(self.type, ' growing!!!')
    def harvest(self):
        print(self.type, ' harvesting!!!')

class Apple(Fruit):
    def __init__(self, treeAge):
        self.treeAge = treeAge
        super(Apple, self).__init__('Apple')

    def plant(self):
        print(self.type, ' planting!!!')
    def grow(self):
        print(self.type, ' growing!!!')
    def harvest(self):
        print(self.type, ' harvesting!!!')

# 抽象類別---園丁
class FruitGardener:
    def __init__(self, type):
        self.type = type
        self.fruitList = []
    @abc.abstractmethod
    def createFruit(self):
        return NotImplemented
    @abc.abstractmethod
    def cultivate(self):
        return NotImplemented

class GrapeGardener(FruitGardener):
    def __init__(self):
        super(GrapeGardener, self).__init__('Grape')
    def createFruit(self, seed):
        self.fruitList.append(Grape(seed))
    def cultivate(self):
        for i in self.fruitList:
            i.plant()
            i.grow()
            i.harvest()

class StrawberryGardener(FruitGardener):
    def __init__(self):
        super(StrawberryGardener, self).__init__('Strawberry')
    def createFruit(self):
        self.fruitList.append(Strawberry())
    def cultivate(self):
        for i in self.fruitList:
            i.plant()
            i.grow()
            i.harvest()

class AppleGardener(FruitGardener):
    def __init__(self):
        super(AppleGardener, self).__init__('Apple')
    def createFruit(self, treeAge):
        self.fruitList.append(Apple(treeAge))
    def cultivate(self):
        for i in self.fruitList:
            i.plant()
            i.grow()
            i.harvest()

# 實體工廠
a = AppleGardener()
a.createFruit(10)
a.createFruit(3)
a.createFruit(2)
a.cultivate()
