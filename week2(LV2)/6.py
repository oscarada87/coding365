import abc

class Employee(abc.ABC):
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def setName(self, name):
        self.name = name
    def setSalary(self, salary):
        self.salary = salary
    def getName(self):
        return self.name
    def getSalary(self):
        return self.salary
    def printInfo(self):
        print('name: {}'.format(self.name))
        print('salary: {}'.format(self.salary))

    @abc.abstractmethod
    def add(employee):
        return NotImplemented
    @abc.abstractmethod
    def remove(employee):
        return NotImplemented
    @abc.abstractmethod
    def getChild(number):
        return NotImplemented
    @abc.abstractmethod
    def myPrint():
        return NotImplemented

class Manager(Employee):
    def __init__(self, name, salary):
        super(Manager, self).__init__(name, salary)
        self.employees = []
    def add(self, employee):
        self.employees.append(employee)
    def remove(self, employee):
        for index, i in enumerate(self.employees):
            if i.getName() == employee.getName():
                employees.pop(index)
            else:
                pass
    def getChild(self, number):
        return self.employees[number - 1]
    def myPrint(self):
        # print('My subordinate')
        for i in self.employees:
            i.printInfo()
    def printInfo(self):
        print('name: {}'.format(self.name))
        print('salary: {}'.format(self.salary))
        self.myPrint()


class Developer(Employee):
    def __init__(self, name, salary):
        super(Developer, self).__init__(name, salary)
    def add(employee):
        print('ERROR!!!')
        print('Developer has no permission')
    def remove(employee):
        print('ERROR!!!')
        print('Developer has no permission')
    def getChild(number):
        print('ERROR!!!')
        print('Developer has no permission')
    def myPrint():
        print('ERROR!!!')
        print('Developer has no permission')
manager1 = Manager('Tom', 80000)
manager2 = Manager('Mary', 70000)
developer1 = Developer('John', 50000)
developer2 = Developer('Kevin', 40000)
manager1.add(developer1)
manager2.add(developer2)
manager1.add(manager2)
manager1.printInfo()
manager2.printInfo()
