import abc

class Lamp(abc.ABC):
    @abc.abstractmethod
    def TurnOn(self):
        return NotImplemented
    @abc.abstractmethod
    def TurnOff(self):
        return NotImplemented

class Button(abc.ABC):
    def __init__(self, lamp):
        self.lamp = lamp
    @abc.abstractmethod
    def GetState(self):
        return NotImplemented
    def Detect(self):
        buttonOn = self.GetState()
        if buttonOn:
            self.lamp.TurnOff()
        else:
            self.lamp.TurnOn()

class DeskLamp(Lamp):
    def __init__(self):
        self.isLampOn = False
    def TurnOn(self):
        self.isLampOn = True
        print('DeskLamp on!!!')
    def TurnOff(self):
        self.isLampOn = False
        print('DeskLamp off!!!')

class PushButton(Button):
    def __init__(self, lamp):
        super(PushButton, self).__init__(lamp)
    def GetState(self):
        if self.lamp.isLampOn:
            return True
        else:
            return False

D = DeskLamp()
P = PushButton(D)
P.Detect()
P.Detect()
P.Detect()
P.Detect()
P.Detect()
P.Detect()
