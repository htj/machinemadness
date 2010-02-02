"""
Board tile definitions.
"""

from machinemadness.game import orientation, movement



class _BaseTile:
    """
    Abstract base tile. Not intended for direct instantiation.
    """
    def __init__(self, lasers=0, walls=None, checkpoint=None):
        self.lasers = lasers
        self.walls  = walls if walls is not None else []
        self.checkpoint = checkpoint # number


    def moveAwayFrom(location, orientation, player, board_state):
        return location, orientation, player, board_state


    def moveInto(location, orientation, player, board_state):
        return location, orientation, player, board_state


    def endTurn(location, orientation, player, board_state):
        return location, orientation, player, board_state



class Blank(_BaseTile):
    """
    Blank tile. Used for filling out board definition for non-square boards.
    Moving into it causes death.
    """
    def moveInto(location, orientation, player, board_state):
        player.kill()



class Regular(_BaseTile):
    """
    Regular tile. Does nothing.
    """
    pass



class Hole(_BaseTile):
    """
    Hole in the board. Moving into it causes death.
    """
    def moveInto(location, orientation, player, board_state):
        player.kill()



class Mover(_BaseTile):
    """
    Moves the player one forward at the end of the turn.
    """
    def __init__(self, orientation, **kwargs):
        _BaseTile.__init__(self, **kwargs)
        self.orientation = orientation


    def endTurn(location, orientation, player, board_state):
        new_location, new_orientation = movement.move(location, orientation, self.orientation)
        return new_location, new_orientation, player, board_state

