
import collections
from blinker import Signal, signal
from blinker.base import symbol


# .toggle._SenderWrapper

# rotating ?

# awaited sender, fake sender

class SenderWrapper:
    # ugly hack
    # maybe pull request to blinker


    __self__ = None
    __func__ = None

    def __init__(self, sender, active=True):
        try:
            self.sender = sender.sender
        except AttributeError:
            self.sender = sender
        if active:
            self.activate()

    def activate(self):
        self.__self__ = self.sender

    def deactivate(self):
        del self.__self__


'''
"fake" senders - an implementation detail

by q index: + 1 | rotate, [0]

'''

# actually, rec.
class _EnqueuedRec:

    def __init__(self, sender, rec, q):
        try:
            self.sender = sender.sender
        except AttributeError:
            self.sender = sender
        self._queue = q

    @property
    def active(self):
        1


class CustomHasherMixin:

    __func__ = __self__ = None

    def hash(self):
        raise NotImplementedError


class OrderedSignalWrapper:
    '''
    (sender, active)
    '''



class Signal_RevolvingReceiver(Signal):
    '''
    1) connect | send
    same obj
    func -> obj
    clone:

    sender(func, q)

    sig.send(sender=obj, ..)

    Wr(sender, active) == sender (by hash)
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


    # when handler worked, swap active signal (modify sender)

    ## (sender, active) == (expected_sender, expected_sender)
    #
    # q: [sender, ..]


    def connect_ordered(self, receiver, sender=Signal.ANY, weak=True):
        assert isinstance(sender, SenderWrapper)
        __sender = SenderWrapper(sender, self._queue)        
        self.connect(receiver, sender=__sender)
        self._queue.append(receiver)



    