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
from server.res.cards.InterfaceCase import InterfaceCase
from server.res.cards.InterfaceCard import InterfaceCard
from server.res.cards.EmptyCase import EmptyCase
from server.res.cards.ObstacleCase import ObstacleCase

class BattleField:

    _instance: 'BattleField' = None
    _map: List[List[InterfaceCase]]
    _troops: List[InterfaceCard]

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        self.initMap()
        self._troops = []

    def getMap(self):
        map: List[List[int]] = []
        for row in range(ROWS):
            line = []
            for column in range(COLUMNS):
                line.append(self._map[row][column].getId())
            map.append(line)
        return map
    
    def updateMap(self):
        self.initMap()
        for troop in self._troops:
            prevX = troop.getPreviousX()
            prevY = troop.getPreviousY()
            if prevX is not None and prevY is not None:
                self._map[prevX][prevY] = EmptyCase(prevX, prevY)

            x = troop.getX()
            y = troop.getY()
            self._map[x][y] = troop
        
    def onUpdateMap(self):
        self.updateMap()
    
    def addTroop(self, troop: InterfaceCard):
        self._troops.append(troop)
        
    def removeTroop(self, troop: InterfaceCard):
        self._troops.remove(troop)
    
    def initMap(self):
        map: List[List[InterfaceCase]] = []
        for row in range(ROWS):
            line = []
            for column in range(COLUMNS):
                line.append(EmptyCase(row, column))
            map.append(line)
        for case in range(ROWS):
            if case in (0, 1, 4, 5, 6, 7, 8, 11, 12):
                map[10][case] = ObstacleCase(row, column)
        self._map = map
        

battle1 = BattleField()
battle2 = BattleField()

print(battle1 is battle2)
