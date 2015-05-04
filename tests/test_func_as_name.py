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


sig1.connect(receiver, sender=name1)
sig1.send(name1)