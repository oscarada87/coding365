# Adaptee Interface
class LegacyModule:
    def click(self):
        pass
    def dbClick(self):
        pass
    def rightClick(self):
        pass

# Adaptee
class oldAPI(LegacyModule):
    def click(self):
        print('click')
    def dbClick(self):
        print('doble click')
    def rightClick(self):
        print('right click')

# Target Interface
class clientInterface:
    def mouseClick(self):
        pass
    def mouseDbClick(self):
        pass
    def mouseRightClick(self):
        pass

#  Target
class client:
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
