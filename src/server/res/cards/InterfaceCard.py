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


    def start_movement_thread(self, path):
        self.movement_thread = threading.Thread(target=self.movement_loop, args=(path,))
        self.movement_thread.start()

    def movement_loop(self, path):
        for x, y in path:
            self.setLocation(x, y)
            time.sleep(self.getMoveSpeedInterval())

    def getMoveSpeedInterval(self):
        match self._SPEED:
            case EnumEntitySpeed.SLOW:
                return 2
            case EnumEntitySpeed.AVERAGE:
                return 1
            case EnumEntitySpeed.FAST:
                return 0.5
            case _:
                return 1
    
    def getTowerFocusCoordoonates(self):
        return TOWER_SIDE_2[0] if self.getSide() == EnumSide.SIDE_1 else TOWER_SIDE_1[0]

    def attack(self):
        pass

    def focusTower():
        return