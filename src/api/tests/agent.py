import unittest
import sys
import os
current_directory = os.path.dirname(os.path.abspath(__file__))
parent_directory = os.path.dirname(current_directory)
grandparent_directory = os.path.dirname(parent_directory)
sys.path.append(grandparent_directory)
from agentTower import AgentTower
from api.enums.TroopEnum import TroopEnum
from server.res.cards.enums.EnumSide import EnumSide

class TestAgentTower(unittest.TestCase):

    def setUp(self):
        self.agent = AgentTower()

    def test_setDeck(self):
        deck = [TroopEnum.ARCHERS, TroopEnum.BABY_DRAGON]
        self.agent.setDeck(deck)
        self.assertEqual(self.agent.getDeck(), deck)

    def test_addDeckCard(self):
        troop = TroopEnum.ARCHERS
        self.agent.addDeckCard(troop)
        self.assertIn(troop, self.agent.getDeck())

    def test_removeDeckCard(self):
        troop = TroopEnum.ARCHERS
        self.agent.addDeckCard(troop)
        self.agent.removeDeckCard(troop)
        self.assertNotIn(troop, self.agent.getDeck())

    def test_selectTeam(self):
        team = EnumSide.SIDE_1
        self.agent.selectTeam(team)
        self.assertEqual(self.agent._team, team)

    def test_generateDeck(self):
        self.agent.generateDeck()
        self.assertEqual(len(self.agent.getDeck()), 8)

if __name__ == '__main__':
    unittest.main()