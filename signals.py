
import collections
from blinker import Signal

class SignalOrderedReceivers(Signal):
    
    def __init__(self, doc=None):
        super().__init__(doc)
        self.receivers = collections.OrderedDict()


class OrderedReceiversMixin:
    
    def __init__(self, doc=None):
        super().__init__(doc)
        self._signal_ordered = Signal()
        self.receivers