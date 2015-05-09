
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


from functools import wraps

def lazyattr(name):
    def decorator(method):
        @wraps(method)
        def getter(self, *args, **kwargs):
            if not hasattr(self, name):
                setattr(self, name, method(self, *args, **kwargs))
            return getattr(self, name)
        return property(getter)
    return decorator



class CustomHasherMixin:

    __func__ = None

    @lazyattr('__self__')
    def hashable_id(self):
        return self.get_hashable_id()

    def get_hashable_id(self):
        raise NotImplementedError


from collections import deque

def get_context(_ctx={}):
    return _ctx

# ord

class _Sender(CustomHasherMixin):

    def get_hashable_id(self):
        '''
        '''
        return True


class _OrdSender(CustomHasherMixin):
    '''
    modifies what to wait for
    (sender, active)
    '''
    def __init__(self, sender):
        self.sender = sender

    @classmethod
    def wrap(cls, func):
        return cls(func)

    @lazyattr('_queue')
    def queue(self):
        return get_context().setdefault('_queue', deque())

    def get_hashable_id(self):
        # calibrate for __self__
        return 0 if self.queue.active is self.sender else 'Inactive'


# encaps: connect_ordered, connect_ordered_via

s_save = _Sender(lambda: 'Srlz.save')


sig = 'pre'

@sig.connect_via(s_save)
def pp(obj):
    print('srls: %s', obj)

sig.connect(rec, rec.sender)

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



    