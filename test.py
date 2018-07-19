class Singleton(object):
    _instance = None
    def __new__(cls, *args, **kw):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kw)
        return cls._instance


class Animal(Singleton):
    def __init__(self):
        self.test = 1
    def change(self):
        self.test = 3
    def change2(self):
        self.test = 78

dog = Animal()
# dog.change()
cat = Animal()
dog.change()
cat.change2()

print(dog.test)
print(cat.test)
