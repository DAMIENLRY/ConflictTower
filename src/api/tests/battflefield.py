import unittest
import sys
import os
current_directory = os.path.dirname(os.path.abspath(__file__))
parent_directory = os.path.dirname(current_directory)
grandparent_directory = os.path.dirname(parent_directory)
sys.path.append(grandparent_directory)

from server.res.BattleField import BattleField
from server.res.cards.BallonCard import BallonCard
from server.res.cards.InterfaceCase import InterfaceCase
from server.res.cards.EmptyCase import EmptyCase
from server.res.cards.ObstacleCase import ObstacleCase
from server.res.cards.states import AttackState
from server.res.cards.enums.EnumSide import EnumSide

class TestBattleField(unittest.TestCase):

    def setUp(self):
        self.battlefield = BattleField.getInstance()
        self.card = BallonCard(EnumSide.SIDE_1, 0, 0)

    def test_getInstance(self):
        self.assertEqual(self.battlefield, BattleField.getInstance())

    def test_initMap(self):
        self.battlefield.initMap()
        self.assertIsInstance(self.battlefield._map, list)
        self.assertIsInstance(self.battlefield._map[0][0], EmptyCase)

    def test_getMap(self):
        self.battlefield.initMap()
        map = self.battlefield.getMap()
        self.assertIsInstance(map, list)
        self.assertIsInstance(map[0][0], int)

    def test_addTroop(self):
        troop = self.card
        self.battlefield.addTroop(troop)
        self.assertIn(troop, self.battlefield._troops)

    def test_removeTroop(self):
        troop = self.card
        self.battlefield.addTroop(troop)
        self.battlefield.removeTroop(troop)
        self.assertNotIn(troop, self.battlefield._troops)

    def test_updateMap(self):
        troop = self.card
        self.battlefield.addTroop(troop)
        self.battlefield.updateMap()
        self.assertIsInstance(self.battlefield._map[troop.getX()][troop.getY()], self.card)

    def test_isOccupiedByOpponent(self):
        troop = self.card
        self.battlefield.addTroop(troop)
        self.battlefield.updateMap()
        self.assertEqual(self.battlefield.isOccupiedByOpponent(troop.getX(), troop.getY()), troop)

    def test_checkAndUpdateCardStates(self):
        troop = self.card
        self.battlefield.addTroop(troop)
        self.battlefield.checkAndUpdateCardStates()
        self.assertIsInstance(troop.state, AttackState)

if __name__ == '__main__':
    unittest.main()