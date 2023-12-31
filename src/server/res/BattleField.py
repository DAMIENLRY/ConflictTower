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
from server.res.cards.ObstacleCase import ObstacleCase
from server.res.cases.DamageCase import DamageCase

from server.res.cards.states.FocusTowerState import FocusTowerState
from server.res.cards.states.AttackState import AttackState

import time
import threading
import queue
from queue import Queue

class BattleField:

    _instance: 'BattleField' = None
    _map: List[List[InterfaceCase]]
    _troops: List[InterfaceCard]

    @classmethod
    def getInstance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    def __init__(self):
        if not self.__class__._instance:
            self.initMap()
            self._troops = []
        else:
            raise Exception("Cette classe est un singleton !")


    def getMap(self):
        map: List[List[int]] = []
        for row in range(ROWS):
            line = []
            for column in range(COLUMNS):
                line.append(self._map[row][column].getId())
            map.append(line)
        return map

    def updateMap(self):
        for troop in self._troops:
            prevX = troop.getPreviousX()
            prevY = troop.getPreviousY()
            if prevX is not None and prevY is not None:
                if not isinstance(self._map[prevX][prevY], DamageCase):
                    self._map[prevX][prevY] = EmptyCase(prevX, prevY)

            x = troop.getX()
            y = troop.getY()
            self._map[x][y] = troop
        print(self.getMap())
        self.checkAndUpdateCardStates()

    def onUpdateMap(self):
        self.updateMap()

    def addTroop(self, troop: InterfaceCard):
        self._troops.append(troop)
        self.onUpdateMap()
        troop.state.handle_request(troop)

    def removeTroop(self, troop: InterfaceCard):
        self._troops.remove(troop)
        self._map[troop._x_position][troop._y_position] = EmptyCase()
        self.onUpdateMap()

    def addDamageCase(self, damageCase):
        x, y = damageCase.getX(), damageCase.getY()
        self._map[x][y] = damageCase
        self.onUpdateMap()

    def removeDamageCase(self, damageCase):
        x, y = damageCase.getX(), damageCase.getY()
        self._map[x][y] = EmptyCase(x, y)
        self.onUpdateMap()

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

    def isOccupiedByOpponent(self,entity,x,y):
        if isinstance(self._map[x][y], InterfaceCard):
            if(entity._side != self._map[x][y]._side):
                return self._map[x][y]
        else:
            return False

    def isCaseEmpty(self,x,y):
        return isinstance(self._map[x][y], EmptyCase)

    def checkAndUpdateCardStates(self):
        for card in self._troops:
            opponent = card.opponentInRange()
            if opponent and not isinstance(card.state, AttackState):
                card.state = AttackState()
                card.state.handle_request(card)
            elif not opponent and not isinstance(card.state, FocusTowerState) and not isinstance(card.state, AttackState):
                card.state = FocusTowerState()
                card.state.handle_request(card)
