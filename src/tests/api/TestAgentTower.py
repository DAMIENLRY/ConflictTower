import unittest

from api.agentTower import AgentTower
from server.res.troops.enums.EnumTroop import EnumTroop
from api.enums.EnumSide import EnumSide

class TestAgentTower(unittest.TestCase):

    def setUp(self):
        self.agent = AgentTower()

    def test_setDeck(self):
        deck = [EnumTroop.ARCHERS, EnumTroop.BABY_DRAGON]
        self.agent.setDeck(deck)
        self.assertEqual(self.agent.getDeck(), deck)

    def test_addDeckCard(self):
        troop = EnumTroop.ARCHERS
        self.agent.addDeckCard(troop)
        self.assertIn(troop, self.agent.getDeck())

    def test_removeDeckCard(self):
        troop = EnumTroop.ARCHERS
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
