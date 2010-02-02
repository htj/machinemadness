"""
movement test
"""

from twisted.trial import unittest

from machinemadness.game import orientation, movement



class MovementTest(unittest.TestCase):

    def setUp(self):
        pass


    def tearDown(self):
        pass


    def testRotation(self):
        l = (0,0)

        # up
        r1 = movement.move(l, orientation.up, movement.rotateleft)
        self.failUnlessEqual(r1, (l, orientation.left))

        r2 = movement.move(l, orientation.up, movement.rotateright)
        self.failUnlessEqual(r2, (l, orientation.right))

        r3 = movement.move(l, orientation.up, movement.uturn)
        self.failUnlessEqual(r3, (l, orientation.down))

        # right
        r4 = movement.move(l, orientation.right, movement.rotateleft)
        self.failUnlessEqual(r4, (l, orientation.up))

        r5 = movement.move(l, orientation.right, movement.rotateright)
        self.failUnlessEqual(r5, (l, orientation.down))

        r6 = movement.move(l, orientation.right, movement.uturn)
        self.failUnlessEqual(r6, (l, orientation.left))

        # down
        r7 = movement.move(l, orientation.down, movement.rotateleft)
        self.failUnlessEqual(r7, (l, orientation.right))

        r8 = movement.move(l, orientation.down, movement.rotateright)
        self.failUnlessEqual(r8, (l, orientation.left))

        r9 = movement.move(l, orientation.down, movement.uturn)
        self.failUnlessEqual(r9, (l, orientation.up))

        # left
        r10 = movement.move(l, orientation.left, movement.rotateleft)
        self.failUnlessEqual(r10, (l, orientation.down))

        r11 = movement.move(l, orientation.left, movement.rotateright)
        self.failUnlessEqual(r11, (l, orientation.up))

        r12 = movement.move(l, orientation.left, movement.uturn)
        self.failUnlessEqual(r12, (l, orientation.right))



    def testMovement(self):

        # forwards
        r1 = movement.move((0,0), orientation.up, movement.forward)
        self.failUnlessEqual(r1, ((0,1), orientation.up))

        r2 = movement.move((0,0), orientation.right, movement.forward)
        self.failUnlessEqual(r2, ((1,0), orientation.right))

        r3 = movement.move((0,0), orientation.down, movement.forward)
        self.failUnlessEqual(r3, ((0,-1), orientation.down))

        r4 = movement.move((0,0), orientation.left, movement.forward)
        self.failUnlessEqual(r4, ((-1,0), orientation.left))

        # backwards
        r5 = movement.move((0,0), orientation.up, movement.backwards)
        self.failUnlessEqual(r5, ((0,-1), orientation.up))

        r6 = movement.move((0,0), orientation.right, movement.backwards)
        self.failUnlessEqual(r6, ((-1,0), orientation.right))

        r7 = movement.move((0,0), orientation.down, movement.backwards)
        self.failUnlessEqual(r7, ((0,1), orientation.down))

        r8 = movement.move((0,0), orientation.left, movement.backwards)
        self.failUnlessEqual(r8, ((1,0), orientation.left))



