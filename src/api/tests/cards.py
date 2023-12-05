import unittest
import sys
import os
current_directory = os.path.dirname(os.path.abspath(__file__))
parent_directory = os.path.dirname(current_directory)
grandparent_directory = os.path.dirname(parent_directory)
sys.path.append(grandparent_directory)
from server.res.cards.BallonCard import BallonCard
from server.res.cards.enums.EnumEntitySpeed import EnumEntitySpeed
from server.res.cards.enums.EnumEntityType import EnumEntityType
from server.res.cards.enums.EnumSide import EnumSide
from server.res.cards.states.StateCard import StateCard

class TestCards(unittest.TestCase):

    def setUp(self):
        self.card = BallonCard(EnumSide.SIDE_1, 0, 0)

    def test_state(self):
        state = StateCard()
        self.card.state = state
        self.assertEqual(self.card.state, state)

    def test_getSide(self):
        self.card._side = EnumSide.SIDE_1
        self.assertEqual(self.card.getSide(), EnumSide.SIDE_1)

    def test_isWithinBounds(self):
        self.assertTrue(self.card.isWithinBounds(5, 5))
        self.assertFalse(self.card.isWithinBounds(-1, 5))
        self.assertFalse(self.card.isWithinBounds(5, -1))
        self.assertFalse(self.card.isWithinBounds(100, 5))
        self.assertFalse(self.card.isWithinBounds(5, 100))

    def test_getMoveSpeedInterval(self):
        self.card._SPEED = EnumEntitySpeed.SPEED_1
        self.assertEqual(self.card.getMoveSpeedInterval(), EnumEntitySpeed.SPEED_1.value)

    def test_setLocation(self):
        self.assertTrue(self.card.setLocation(5, 5))
        self.assertFalse(self.card.setLocation(-1, 5))
        self.assertFalse(self.card.setLocation(5, -1))
        self.assertFalse(self.card.setLocation(100, 5))
        self.assertFalse(self.card.setLocation(5, 100))

    def test_opponentInRange(self):
        self.card._RANGE = 1
        self.card._x_position = 5
        self.card._y_position = 5
        self.assertIsNone(self.card.opponentInRange())

if __name__ == '__main__':
    unittest.main()