import unittest
import sys
import os
import random
current_directory = os.path.dirname(os.path.abspath(__file__))
parent_directory = os.path.dirname(current_directory)
grandparent_directory = os.path.dirname(parent_directory)
sys.path.append(grandparent_directory)

from server.res.troops.enums.EnumTroop import EnumTroop
from server.res.troops.enums.EnumEntitySpeed import EnumEntitySpeed
from api.enums.EnumSide import EnumSide
from server.res.troops.states.FocusTowerState import FocusTowerState
from server.res.troops.states.AttackState import AttackState

class InterfaceTroopsTest(unittest.TestCase):

    def setUp(self):
        troops = list(EnumTroop)
        random.shuffle(troops)
        self.cards = []
        for troop in troops:
            if troop is EnumTroop.BALLON or troop is EnumTroop.BOWLER:
                self.cards.append(troop.value(EnumSide.SIDE_1, 0, 0))
            else:
                self.cards.append(troop.value())

    def test_state(self):
        for card in self.cards:
            state = random.choice([AttackState(), FocusTowerState()])
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
            card._SPEED = EnumEntitySpeed.AVERAGE
            self.assertEqual(card.getMoveSpeedInterval(), EnumEntitySpeed.AVERAGE.value)

    def test_setLocation(self):
        print("test_setLocation")
        for card in self.cards:
            card.setLocation(5, 5)
            self.assertTrue(card.isWithinBounds(5, 5))

    def test_opponentInRange(self):
        for card in self.cards:
            card._RANGE = 1
            card._x_position = 5
            card._y_position = 5
            self.assertFalse(card.opponentInRange())

if __name__ == '__main__':
    unittest.main()