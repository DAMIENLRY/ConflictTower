import unittest
import sys
import os
import random
current_directory = os.path.dirname(os.path.abspath(__file__))
parent_directory = os.path.dirname(current_directory)
grandparent_directory = os.path.dirname(parent_directory)
sys.path.append(grandparent_directory)
from server.res.cards.BallonCard import BallonCard
from server.res.cards.enums.EnumEntitySpeed import EnumEntitySpeed
from server.res.cards.enums.EnumEntityType import EnumEntityType
from server.res.cards.enums.EnumSide import EnumSide
from server.res.cards.states.StateCard import StateCard
from api.enums.TroopEnum import TroopEnum

class TestCards(unittest.TestCase):

    def setUp(self):
        troops = list(TroopEnum)
        random.shuffle(troops)
        self.cards = [troop.value(EnumSide.SIDE_1, 0, 0) for troop in troops]

    def test_state(self):
        for card in self.cards:
            state = StateCard()
            card.state = state
            self.assertEqual(card.state, state)

    def test_getSide(self):
        for card in self.cards:
            card._side = EnumSide.SIDE_1
            self.assertEqual(card.getSide(), EnumSide.SIDE_1)

    def test_isWithinBounds(self):
        for card in self.cards:
            self.assertTrue(card.isWithinBounds(5, 5))
            self.assertFalse(card.isWithinBounds(-1, 5))
            self.assertFalse(card.isWithinBounds(5, -1))
            self.assertFalse(card.isWithinBounds(100, 5))
            self.assertFalse(card.isWithinBounds(5, 100))

    def test_getMoveSpeedInterval(self):
        for card in self.cards:
            card._SPEED = EnumEntitySpeed.SPEED_1
            self.assertEqual(card.getMoveSpeedInterval(), EnumEntitySpeed.SPEED_1.value)

    def test_setLocation(self):
        for card in self.cards:
            self.assertTrue(card.setLocation(5, 5))
            self.assertFalse(card.setLocation(-1, 5))
            self.assertFalse(card.setLocation(5, -1))
            self.assertFalse(card.setLocation(100, 5))
            self.assertFalse(card.setLocation(5, 100))

    def test_opponentInRange(self):
        for card in self.cards:
            card._RANGE = 1
            card._x_position = 5
            card._y_position = 5
            self.assertIsNone(card.opponentInRange())

if __name__ == '__main__':
    unittest.main()