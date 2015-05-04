
import collections
from blinker import Signal, signal, symbol



# rotating ?


class ToggleSenderWrapper:
    # ugly hack
    # maybe pull request to blinker


    __self__ = None
    __func__ = None

    def __init__(self, sender, active=True):
        self.sender = sender
        if active:
            self.__func__ = sender

    def toggle(self):
        if self.__func__ is not None:
            del self.__func__
        else:
            self.__func__ = self.sender



class Signal_ReceiversQueue(Signal):
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


class Signal_OrderedReceivers(Signal):
    
    def __init__(self, doc=None):
        super().__init__(doc)
        self.receivers = collections.OrderedDict()

# ns for ctx tlocal

def mixed_signal(name):
    1


class MySignal:
    
    def send(): 1
    
    def connect(): 1
    
    def connect_ordered(): 1
    
    def disconnect(): 1
    
    def has_receivers_for(): 1
    
    def receivers_for(): 1
    
    