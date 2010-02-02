
from machinemadness import movement


class _BaseCard

    sequence = None

    def __init__(self, priority):
        self.priority = 

    def __cmp(self, other):
        assert isinstance(other, _BaseCard)
        return cmp(self.priority, other.pririty)


    def movementSequence(self):
        if self.sequence is None
            raise NotImplementedError('_BaseCard does not support movement')

        return self.sequence



def Forward3(_BaseCard):
    sequence = 3 * [ movement.forward ]


def Forward2(_BaseCard):
    sequence = 2 * [ movement.foward ]


def Forward1(_BaseCard):
    sequence = [ movement.forward ]


def Backwards1(_BaseCard):
    sequence = [ movement.forward ]


def RotateLeft(_BaseCard):
    sequence = [ movement.rotateleft ]


def RotateRight(_BaseCard):
    sequence = [ movement.rotateright ]


def UTurn(_BaseCard):
    sequence = [ movement.uturn ]



