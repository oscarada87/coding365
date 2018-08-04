import abc

# 抽象類別---水果
class Fruit:
    def __init__(self, type):
        self.type = type
    @abc.abstractmethod
    def plant(self):
        return NotImplemented
    @abc.abstractmethod
    def protect(self):
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
    def protect(self):
        print(self.type, ' protecting!!!')
    def grow(self):
        print(self.type, ' growing!!!')
    def harvest(self):
        print(self.type, ' harvesting!!!')

class Strawberry(Fruit):
    def __init__(self):
        super(Strawberry, self).__init__('Strawberry')

    def plant(self):
        print(self.type, ' planting!!!')
    def protect(self):
        print(self.type, ' protecting!!!')
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
    def protect(self):
        print(self.type, ' protecting!!!')
    def grow(self):
        print(self.type, ' growing!!!')
    def harvest(self):
        print(self.type, ' harvesting!!!')

# 抽象類別---蔬菜
class Veggie:
    def __init__(self, type):
        self.type = type
    @abc.abstractmethod
    def plant(self):
        return NotImplemented
    @abc.abstractmethod
    def grow(self):
        return NotImplemented
    @abc.abstractmethod
    def deworm(self):
        return NotImplemented
    @abc.abstractmethod
    def harvest(self):
        return NotImplemented

class Cabbage(Veggie):
    def __init__(self):
        super(Cabbage, self).__init__('Cabbage')

    def plant(self):
        print(self.type, ' planting!!!')
    def grow(self):
        print(self.type, ' growing!!!')
    def deworm(self):
        print(self.type, ' deworming!!!')
    def harvest(self):
        print(self.type, ' harvesting!!!')

class Lettuce(Veggie):
    def __init__(self):
        super(Lettuce, self).__init__('Lettuce')

    def plant(self):
        print(self.type, ' planting!!!')
    def grow(self):
        print(self.type, ' growing!!!')
    def deworm(self):
        print(self.type, ' deworming!!!')
    def harvest(self):
        print(self.type, ' harvesting!!!')

# 抽象類別---園丁
class Gardener:
    def __init__(self, type):
        self.type = type
        self.fruitList = []
        self.veggieList = []
    @abc.abstractmethod
    def createFruit(self):
        return NotImplemented
    @abc.abstractmethod
    def createVeggie(self):
        return NotImplemented
    @abc.abstractmethod
    def cultivateAll(self):
        return NotImplemented

# 實體工廠
class NorthernGardener(Gardener):
    def __init__(self):
        super(NorthernGardener, self).__init__('Northern')

    def createFruit(self, name, seed = None, treeAge = None):
        if name == 'Grape':
            self.fruitList.append(Grape(seed))
        elif name == 'Strawberry':
            self.fruitList.append(Strawberry())
        elif name == 'Apple':
            self.fruitList.append(Apple(treeAge))
        else:
            print('ERROR -- InValid Input')

    def createVeggie(self, name):
        if name == 'Cabbage':
            self.veggieList.append(Cabbage())
        elif name == 'Lettuce':
            self.veggieList.append(Lettuce())
        else:
            print('ERROR -- Invalid Input')

    def cultivateAll(self):
        print('I\'m a ',self.type, 'gardener')
        for i in self.fruitList:
            i.plant()
            i.protect()
            i.grow()
            i.harvest()
        for i in self.veggieList:
            i.plant()
            i.grow()
            i.deworm()
            i.harvest()

class TropicalGardener(Gardener):
    def __init__(self):
        super(TropicalGardener, self).__init__('Tropical')

    def createFruit(self, name, seed = None, treeAge = None):
        if name == 'Grape':
            self.fruitList.append(Grape(seed))
        elif name == 'Strawberry':
            self.fruitList.append(Strawberry())
        elif name == 'Apple':
            self.fruitList.append(Apple(treeAge))
        else:
            print('ERROR -- Not Valid Input')

    def createVeggie(self, name):
        if name == 'Cabbage':
            self.veggieList.append(Cabbage())
        elif name == 'Lettuce':
            self.veggieList.append(Lettuce())
        else:
            print('ERROR -- Invalid Input')

    def cultivateAll(self):
        print('I\'m a ',self.type, 'gardener')
        for i in self.fruitList:
            i.plant()
            i.protect()
            i.grow()
            i.harvest()
        for i in self.veggieList:
            i.plant()
            i.grow()
            i.deworm()
            i.harvest()

a = NorthernGardener()
b = TropicalGardener()
a.createFruit('Apple', 3)
a.createVeggie('Cabbage')
a.createFruit('Strawberry')
b.createFruit('Grape', False)
b.createVeggie('Lettuce')
b.createFruit('Apple', 5)
a.cultivateAll()
b.cultivateAll()
