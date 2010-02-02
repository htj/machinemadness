"""
movement test
"""

from twisted.trial import unittest

from machinemadness.game import orientation, movement, boarddefinition
from machinemadness.data import boards



class BoardTest(unittest.TestCase):

    def setUp(self):
        self.board_def = boarddefinition.createBoard(boards.BORING1)


    def tearDown(self):
        pass


    def testBoardMovement(self):

        pass




