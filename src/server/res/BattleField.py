from typing import List
import sys
import os

# Chemin absolu du répertoire parent de conflictTowers.py
current_file = os.path.abspath(__file__)  # Chemin actuel du script en cours
parent_directory = os.path.dirname(os.path.dirname(os.path.dirname(current_file)))  # Chemin du répertoire parent du parent du parent
sys.path.append(parent_directory)  # Ajoute le répertoire parent au chemin de recherche

# Maintenant, vous pouvez importer COLUMNS et ROWS depuis conflictTowers
from api.globaleVariable import COLUMNS, ROWS

# Maintenant, importez InterfaceCard
from server.res.cards.InterfaceCard import InterfaceCard

class BattleField:

    _instance: 'BattleField' = None
    _map: List[List[int]]
    _troops: List #//: List[InterfaceCard]

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        map = [[0 for j in range(COLUMNS)] for i in range(ROWS)]
        for i in range(COLUMNS):
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
