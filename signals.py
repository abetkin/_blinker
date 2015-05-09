
import collections
from blinker import Signal, signal
from blinker.base import symbol

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

from blinker.base import hashable_identity

class CustomHasherWrapper:

    def __init__(self, wrapped):
        self.wrapped = wrapped

    @property
    def __self__(self):
        return hashable_identity(self.wrapped)

    @property
    def __func__(self):
        return self.custom_hash()

    def custom_hash(self):
        raise NotImplementedError


class TogglingSenderWrapper(CustomHasherWrapper):
    '''
    Active / inactive.
    '''
    def custom_hash(self):
        return self.is_active()

    def is_active(self):
        raise NotImplementedError


from collections import deque

def get_context(_ctx={}):
    return _ctx

# ord


# wrappers.py

class SimpleSenderWrapper(CustomHasherWrapper):
    '''
    Always active.
    '''
    def is_active(self):
        return True

class OrderQueueSenderWrapper(TogglingSenderWrapper):

    @lazyattr('_queue')
    def queue(self):
        return get_context().setdefault('_events_queue', deque())

    def is_active(self):
        '''return self.queue.active is self.sender
        '''





class FunctionSignal(Signal):
    '''
    The pre- and post-execution signals.
    Senders of these are functions (wrapped).
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



    