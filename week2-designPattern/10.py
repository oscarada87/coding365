import abc

class Duck:
    def __init__(self, type, quackBehavior = None, flyBehavior = None):
        self.type = type
        self.quackBehavior = quackBehavior
        self.flyBehavior = flyBehavior

    def setQuackBehavior(self, quackBehavior):
        self.quackBehavior = quackBehavior

    def setFlyBehavior(self, flyBehavior):
        self.flyBehavior = flyBehavior

    def quack(self):
        self.quackBehavior.quack()

    def fly(self):
        self.flyBehavior.fly()

class QuackBehavior(abc.ABC):
    def quack(self):
        return NotImplemented

class Mute(QuackBehavior):
    def quack(self):
        print('I can\'t quack!!!')

class NormalQuack(QuackBehavior):
    def quack(self):
        print('Quack!!!Quack!!!')

class Howl(QuackBehavior):
    def quack(self):
        print('枝枝!!!枝枝!!!')

class FlyBehavior(abc.ABC):
    def fly(self): 
        return NotImplemented

class UnableFly(FlyBehavior):
    def fly(self):
        print('I can\'t fly!!!')

class NormalFly(FlyBehavior):
    def fly(self):
        print('I am flying!!!')

class TempFly(FlyBehavior):
    def fly(self):
        print('I can only fly 5 seconds!!!')

Decoy = Duck('decoy', Mute(), UnableFly())
Rubber = Duck('rubber', Howl(), TempFly())
Decoy.fly()
Decoy.quack()
Rubber.fly()
Rubber.quack()
