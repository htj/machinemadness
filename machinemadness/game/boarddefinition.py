
from machinemadness.game import orientation, tile


class BoardDefinition:

    def __init__(self, board, checkpoints, initial_markers):
        self.board = board
        self.checkpoints = checkpoints
        self.initial_markers = initial_markers



def createBoard(definition, deftype=1):

    assert deftype == 1

    lines = definition.split('|')

    board = {}
    markers = {}
    checkpoints = 0

    for x in range(len(lines)):
        line = lines[x]
        for y in range(len(line)):
            c = line[y]

            if   c == 'c': t = tile.Regular(checkpoint=1) ; checkpoints += 1
            elif c == ' ': t = tile.Regular()
            elif c == '>': t = tile.Mover(orientation.right)
            elif c == '<': t = tile.Mover(orientation.left)
            elif c == 'v': t = tile.Mover(orientation.down)
            elif c == 'a': t = tile.Mover(orientation.up)
            elif c == '1': t = tile.Regular() ; markers[1] = x,y
            elif c == '2': t = tile.Regular() ; markers[2] = x,y
            elif c == '3': t = tile.Regular() ; markers[3] = x,y
            elif c == '4': t = tile.Regular() ; markers[4] = x,y

            else:
                raise ValueError('invalid tile code: %s' % c)

            board[x,y] = t


    return BoardDefinition(board, checkpoints, markers)

