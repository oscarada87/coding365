import abc

class Timer:
    def register(self, timeout, timeOutId, client):
        print('registing...')
        print('timeout: ', timeout)
        print('timeOutId: ', timeOutId)


class TimerClient(abc.ABC):
    self.timer = Timer(timeout, timeOutId, self)
    @abc.abstractmethod
    def TimeOut(self, timeOutId):
        return NotImplemented
    def needNotify(self, timeout, timeOutId):
        timer.register(timeout, timeOutId, self)

class DoorTimerAdapter(TimerClient):
    def __init__(self, timedDoor, timer):
        self.timedDoor = timedDoor
        self.timer = timer


class Door(abc.ABC):
    def __init__(self, state = 'Unknown'):
        self.state = state
    def close(self):
        self.state = 'close'
        print('Closing the door!!!')
    def open(self):
        self.state = 'open'
        print('Opening the door!!!')
    def isDoorOpen(self):
        if self.state == 'open':
            return True
        elif self.state == 'close':
            return False
        else:
            print('Error state unknown')
            return 0
    @abc.abstractmethod
    def enter(self):
        return NotImplemented

class TimedDoor(Door):
    def __init__(self):
        self.timerClient = timerClient
        self.timerID = timerID
        self.timeout = timeout
    def enter(self):
        timerClient.needNotify(timeout, timerID + 1)
    def setAdater(self, TimerClient):
        pass
    def doorTimeOut(self, timeOutId):
        pass
