from abc import ABC
from .InterfaceCase import InterfaceCase
from .enums.EnumEntitySpeed import EnumEntitySpeed
from .enums.EnumEntityType import EnumEntityType
from .enums.EnumSide import EnumSide
from .states.StateCard import StateCard
import time
import sys
import os
import threading
import api.towerFinder as tf

from api.globaleVariable import COLUMNS, ROWS, TOWER_SIDE_1, TOWER_SIDE_2

# Obtenez le chemin du répertoire parent de ConflictTower (c'est-à-dire le dossier contenant ConflictTower)
current_file = os.path.abspath(__file__)  # Chemin actuel du script en cours
parent_directory = os.path.dirname(current_file) # Chemin du répertoire parent
sys.path.append(parent_directory)  # Ajoute le répertoire parent au chemin de recherche


class InterfaceCard(InterfaceCase):

    _SPEED: EnumEntitySpeed
    _RANGE: int
    _ATTAQUE_SPEED: EnumEntitySpeed
    _TYPE: EnumEntityType
    _HEALTH_POINT: int
    _POINT: int
    _state: StateCard
    _side: EnumSide
    _stop_movement = True
    _battlefield = None

    @property
    def state(self):
        return self._state
    
    @state.setter
    def state(self, new_state: StateCard):
        self._state = new_state

    def getSide(self) -> EnumSide:
        return self._side

    def isWithinBounds(self, x, y):
        return 0 <= x < ROWS and 0 <= y < COLUMNS



    def start_movement_thread(self):
        path = tf.pathToTower((self.getX(),self.getY()),self.getTowerFocusCoordoonates())
        self.movement_thread = threading.Thread(target=self.movement_loop, args=(path,))
        self.movement_thread.start()

    def stop_movement_thread(self):
        self._stop_movement = True

    def movement_loop(self, path):
        self._stop_movement = False
        for x, y in path:
            if self._stop_movement:
                break
            self.setLocation(x, y)
            time.sleep(self.getMoveSpeedInterval())
        print("Movement thread stopped.")



    def getMoveSpeedInterval(self):
        return self._SPEED.value
    
    def getTowerFocusCoordoonates(self):
        return TOWER_SIDE_2[0] if self.getSide() == EnumSide.SIDE_1 else TOWER_SIDE_1[0]
    
    def setLocation(self, x: int, y: int):    
        if x>=1 and x<=ROWS-1 and y>=0 and y<=COLUMNS-1:
            if self._x_position and self._y_position:
                self._x_prev_position = self._x_position
                self._y_prev_position = self._y_position
            self._x_position = x
            self._y_position = y
            self._battlefield.onUpdateMap()
        else:
            return False

    def opponentInRange(self):
        offsets = [
            (dx, dy) for dx in range(-self._RANGE, self._RANGE + 1) 
            for dy in range(-self._RANGE, self._RANGE + 1) 
            if not (dx == 0 and dy == 0)
        ]

        for dx, dy in offsets:
            targetX, targetY = dx + self._x_position, dy + self._y_position

            if self.isWithinBounds(targetX, targetY):
                opponent = self._battlefield.isOccupiedByOpponent(targetX, targetY)
                if opponent:
                    return opponent

        return False