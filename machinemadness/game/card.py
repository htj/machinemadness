
from machinemadness.game import movement


class _BaseCard:

    sequence = None

    def __init__(self, priority):
        self.priority = priority

    def __cmp(self, other):
        assert isinstance(other, _BaseCard)
        return cmp(self.priority, other.pririty)


    def movementSequence(self):
        if self.sequence is None:
            raise NotImplementedError('_BaseCard does not support movement')

        return self.sequence



class Forward3(_BaseCard):
    sequence = 3 * [ movement.forward ]


class Forward2(_BaseCard):
    sequence = 2 * [ movement.forward ]


class Forward1(_BaseCard):
    sequence = [ movement.forward ]


class Backwards1(_BaseCard):
    sequence = [ movement.backwards ]


class RotateLeft(_BaseCard):
    sequence = [ movement.rotateleft ]


class RotateRight(_BaseCard):
    sequence = [ movement.rotateright ]


class UTurn(_BaseCard):
    sequence = [ movement.uturn ]



