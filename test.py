import abc

# Adaptee Interface
class LegacyModule(metaclass = abc.ABCMeta):
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

#  Target
class client(clientInterface):
    def __init__(self, mouse = None):
        self.mouse = mouse
    def mouseClick(self):
        self.mouse.mouseClick()
    def mouseDbClick(self):
        self.mouse.mouseDbClick()
    def mouseRightClick(self):
        self.mouse.mouseRightClick()

# Adapter
class Adapter(clientInterface):
    def __init__(self, old = None):
        self.old = old
    def mouseClick(self):
        return self.old.click()
    def mouseDbClick(self):
        return self.old.dbClick()
    def mouseRightClick(self):
        return self.old.rightClick()


old = oldAPI()
adapter = Adapter(old)
c = client(Adapter(oldAPI()))

c.mouseClick()
c.mouseDbClick()
c.mouseRightClick()
