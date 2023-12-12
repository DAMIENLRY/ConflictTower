import unittest
from server.res.cards.BallonCard import BallonCard
from server.res.BattleField import BattleField
from server.res.cards.enums.EnumSide import EnumSide

class TestBattleField(unittest.TestCase):

    def test_add_and_get_card(self):
        battlefield = BattleField()
        ballon_card = BallonCard(EnumSide.BLUE, 1, 1)
        battlefield.add_card(ballon_card, 1, 1)
        self.assertEqual(battlefield.get_card(1, 1), ballon_card)

if __name__ == '__main__':
    unittest.main()
