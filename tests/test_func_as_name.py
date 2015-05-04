from blinker import Namespace

ns = Namespace()

def name1():
    return 1

def name2():
    return 2

sig1 = ns.signal(name1)
sig2 = ns.signal(name2)

# @sig1.connect
def receiver(sender):
    print('sender %s' % sender)


from signals import SenderWrapper
ToggledSender = SenderWrapper


# def clone(sender):

from blinker.base import hashable_identity



cloned1 = ToggledSender(name1)
cloned2 = ToggledSender(cloned1)

print(hashable_identity(cloned1) == hashable_identity(cloned2))

sig1.connect(receiver, sender=cloned1)
cloned2.deactivate()
cloned2.activate()
sig1.send(cloned2)