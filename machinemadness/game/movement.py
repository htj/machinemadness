"""
Movement operations, i.e., rotation and movement.
"""

from machinemadness.game.orientation import up, right, down, left
from machinemadness.game import orientation



class _Rotation:
    # not meant for instantiation

    direction = {
        # up
        ('u', 'l') : left,
        ('u', 'r') : right,
        ('u', 'u') : down,
        # right
        ('r', 'l') : up,
        ('r', 'r') : down,
        ('r', 'u') : left,
        # down
        ('d', 'l') : right,
        ('d', 'r') : left,
        ('d', 'u') : up,
        # left
        ('l', 'l') : down,
        ('l', 'r') : up,
        ('l', 'u') : right,
    }

    def __init__(self, state):
        # left, right, u-turn
        assert state in ['l', 'r', 'u']
        self.state = state


    def rotate(self, orient):
        return self.direction[(orient.state, self.state)]



class _Movement:
    # not meant for instantiation

    def __init__(self, state):
        # forwards, backwards - sidestepping should be easy to add
        assert state in ['f', 'b']
        self.state = state


    def move(self, location, orient):
        x,y = location

        if orient == up:
            y = y+1 if self.state == 'f' else y-1
        if orient == right:
            x = x+1 if self.state == 'f' else x-1
        if orient == down:
            y = y-1 if self.state == 'f' else y+1
        if orient == left:
            x = x-1 if self.state == 'f' else x+1

        return (x, y)



rotateleft  = _Rotation('l')
rotateright = _Rotation('r')
uturn       = _Rotation('u')

forward     = _Movement('f')
backwards   = _Movement('b')



def move(location, orient, action):

    assert isinstance(location, tuple)
    assert isinstance(orient, orientation._Orientation)
    assert isinstance(action, _Rotation) or isinstance(action, _Movement)

    if isinstance(action, _Rotation):
        new_orient = action.rotate(orient)
        return location, new_orient

    if isinstance(action, _Movement):
        new_location = action.move(location, orient)
        return new_location, orient

