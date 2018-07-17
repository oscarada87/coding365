import abc

class Lamp:
    @abc.abstractmethod
    def TurnOn(self):
        return NotImplemented
    @abc.abstractmethod
    def TurnOff(self):
        return NotImplemented

class Button:
    def __init__(self, lamp, pushed):
        self.lamp = lamp
        self.pushed = pushed
    @abc.abstractmethod
    def GetState(self):
        return NotImplemented
    def Detect(self):
        buttonOn = self.GetState()
        if buttonOn:
            self.lamp.TurnOn()
        else:
            self.lamp.TurnOff()

class DeskLamp(Lamp):
    def TurnOn(self):
        print('DeskLamp on!!!')
    def TurnOff(self):
        print('DeskLamp off!!!')

class PushButton(Button):
    def __init__(self, lamp, pushed = True):
        super(PushButton, self).__init__(lamp, pushed)
    def GetState(self):
        if self.pushed:
            return True
        else:
            return False
    def PushButton(self):
        self.Detect()
        if self.pushed:
            self.pushed = False
        else:
            self.pushed = True

D = DeskLamp()
P = PushButton(D)
P.PushButton()
P.PushButton()
P.PushButton()
P.PushButton()
P.PushButton()
P.PushButton()
P.PushButton()
P.PushButton()
P.PushButton()
P.PushButton()
