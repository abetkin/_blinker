
import collections
from blinker import Signal, signal
from blinker.base import symbol


# .toggle._SenderWrapper

# rotating ?


class SenderWrapper:
    # ugly hack
    # maybe pull request to blinker


    __self__ = None
    __func__ = None

    def __init__(self, sender, active=True):
        # follow __self__ links
        self.sender = sender
        if active:
            self.activate()

    def activate(self):
        self.__self__ = self.sender

    def deactivate(self):
        del self.__self__
        


class ExtSignal(Signal):
    '''
    TODO
    '''

    def __init__(self, doc=None):
        super().__init__(doc)
        self._queue = collections.deque()

    # def 

    def send(self, *sender, **kwargs):
        super().send(*sender, **kwargs)
        assert sender, "Sender is the function being executed"
        sender[0]
        awaited_sender = self._queue[-1]

    # def connect_ordered(self, receiver, sender=ANY, weak=True):
    #     cloned_sender = SenderWrapper(sender, active=False)


# ns for ctx tlocal

def mixed_signal(name):
    1


class _MySignal:
    
    def send(): 1
    
    def connect(): 1
    
    def connect_ordered(): 1
    
    def disconnect(): 1
    
    def has_receivers_for(): 1
    
    def receivers_for(): 1
    
    