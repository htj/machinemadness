"""
Orientation, i.e., which way is a robot facing.
"""


class _Orientation:
    # not meant for instantiation

    def __init__(self, state):
        # up, right, down, left
        assert state in ['u', 'r', 'd', 'l']
        self.state = state


up          = _Orientation('u')
right       = _Orientation('r')
down        = _Orientation('d')
left        = _Orientation('l')

