"""
movement test
"""

from twisted.trial import unittest

from machinemadness.game import card, orientation, movement



class CardTest(unittest.TestCase):

    def setUp(self):
        pass


    def tearDown(self):
        pass


    def testCardMovement(self):
        l = (0,0)
        o = orientation.up

        c1 = card.Forward3(0)
        c2 = card.RotateLeft(0)
        c3 = card.Backwards1(0)
        c4 = card.Forward2(0)
        c5 = card.RotateRight(0)
        c6 = card.Forward1(0)
        c7 = card.UTurn(0)

        sequence = [c1, c2, c3, c4, c5, c6, c7]

        for crd in sequence:
            for action in crd.movementSequence():
                l, o = movement.move(l, o, action)

        self.failUnlessEqual((l,o), ((-1,4), orientation.down))

