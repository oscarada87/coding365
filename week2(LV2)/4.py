import abc

# Adaptee Interface
class LegacyModule(abc.ABC):
    @abc.abstractmethod
    def click(self):
        return NotImplemented
    @abc.abstractmethod
    def dbClick(self):
        return NotImplemented
    @abc.abstractmethod
    def rightClick(self):
        return NotImplemented

# Adaptee
class oldAPI(LegacyModule):
    def click(self):
        print('click')
    def dbClick(self):
        print('doble click')
    def rightClick(self):
        print('right click')

# Target Interface
class clientInterface(metaclass = abc.ABCMeta):
    @abc.abstractmethod
    def mouseClick(self):
        return NotImplemented
    @abc.abstractmethod
    def mouseDbClick(self):
        return NotImplemented
    @abc.abstractmethod
    def mouseRightClick(self):
        return NotImplemented

# Adapter
class Adapter(clientInterface):
    def __init__(self, old):
        self.old = old
    def mouseClick(self):
        return self.old.click()
    def mouseDbClick(self):
        return self.old.dbClick()
    def mouseRightClick(self):
        return self.old.rightClick()

# old = LegacyModule()
old = oldAPI()
adapter = Adapter(old)
c = Adapter(oldAPI())

c.mouseClick()
c.mouseDbClick()
c.mouseRightClick()
