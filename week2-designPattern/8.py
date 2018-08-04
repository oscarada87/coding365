
class Pet:
    def __init__(self, type):
        self.type = type
    def eat(self):
        print(self.type,'餵食')
    def walk(self):
        print(self.type,'帶去散步')
    def sleep(self):
        print(self.type,'要睡覺')

class Dog(Pet):
    def __init__(self):
        super(Dog, self).__init__('Dog')
class Cat(Pet):
    def __init__(self):
        super(Cat, self).__init__('Cat')
class Bird(Pet):
    def __init__(self):
        super(Bird, self).__init__('Bird')

class PetFactory:
    def __init__(self):
        self.petType = ['Dog', 'Cat', 'Bird']

    def createPet(self, type):
        if type == self.petType[0]:
            return Dog()
        elif type == self.petType[1]:
            return Cat()
        elif type == self.petType[2]:
            return Bird()
        else:
            print('ERROR')
            print('No this type')
            return 0

factory = PetFactory()
petList = []
petList.append(factory.createPet('Cat'))
petList.append(factory.createPet('Dog'))
petList.append(factory.createPet('Bird'))

for i in petList:
    i.walk()
