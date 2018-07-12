class component(object):
    def __init__(self, name, cost, id):
        self.__name = name
        self.__cost = cost
        self.__id = id
    def getName(self):
        return self.__name
    def getCost(self):
        return self.__cost
    def getId(self):
        return self.__id
    def info(self):
        print('id:', self.__id)
        print('name:', self.__name)
        print('cost:', self.__cost)


class CPU(component):
    def __init__(self, name, cost, id):
        super(CPU, self).__init__(name, cost, id)

    def test(self):
        print('test')

A = CPU('AAA', 20, 1)
A.info()
A.test()
