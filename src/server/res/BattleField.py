from typing import List
#from ...api.conflictTowers import COLUMNS, ROWS

from cards.InterfaceCard import InterfaceCard

class BattleField:

    _instance: 'BattleField' = None
    _map: List[List[int]]
    _troops: List[InterfaceCard]

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        map = [[0 for j in range(13)] for i in range(21)]
        for i in range(13):
            if i not in (2, 3, 9, 10):
                map[10][i] = 1
        self._map = map
        self._troops = []

    def getMap(self):
        return self._map
    
    def updateMap(self):
        for troop in self._troops:
            x = troop.getX()
            y = troop.getY()
            self._map[x][y] = troop.ID
        
    def onUpdateMap(self):
        self.updateMap()



battle1 = BattleField()
battle2 = BattleField()

print(battle1 is battle2)
