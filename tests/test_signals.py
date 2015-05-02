
from signals import SignalOrderedReceivers
from util import case

sig = SignalOrderedReceivers()

class Receiver(object):
    
    @property
    def bucket(self):
        return self.__dict__.setdefault('_bucket', [])

    @bucket.deleter
    def bucket(self):
        del self._bucket

    def handler1(self, sender):
        self.bucket.append(1)
    
    def handler2(self, sender):
        self.bucket.append(2)

    def handler3(self, sender):
        self.bucket.append(3)


obj = Receiver()

sig.connect(obj.handler2)
sig.connect(obj.handler1)
sig.connect(obj.handler3)

for i in range(10):
    sig.send('sender')
    case.assertEqual(obj.bucket, [2, 1, 3])
    del obj.bucket