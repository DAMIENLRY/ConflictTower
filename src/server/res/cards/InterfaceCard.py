from abc import ABC
from .InterfaceCase import InterfaceCase
from .enums.EnumEntitySpeed import EnumEntitySpeed
from .enums.EnumEntityType import EnumEntityType
from .states.StateCard import StateCard
import time
import sys
import os

# Obtenez le chemin du répertoire parent de ConflictTower (c'est-à-dire le dossier contenant ConflictTower)
current_file = os.path.abspath(__file__)  # Chemin actuel du script en cours
parent_directory = os.path.dirname(current_file) # Chemin du répertoire parent
sys.path.append(parent_directory)  # Ajoute le répertoire parent au chemin de recherche

class InterfaceCard(StateCard, InterfaceCase):

    _SPEED: EnumEntitySpeed
    _RANGE: float
    _ATTAQUE_SPEED: EnumEntitySpeed
    _TYPE: EnumEntityType
    _HEALTH_POINT: int
    _POINT: int
    _state: StateCard

    @property
    def getState(self) -> StateCard:
        return self._state

    @property
    def setState(self, state) -> StateCard:
        self._state = state

    def move(self, x: int, y: int) -> None:
        if x < -1 or x > 1 or y < -1 or y > 1:
            return

        if self.SPEED == EnumEntitySpeed["SLOW"]:
            time.sleep(2)
        if self.SPEED == EnumEntitySpeed["AVERAGE"]:
            time.sleep(1)
        if self.SPEED == EnumEntitySpeed["FAST"]:
            time.sleep(0.5)
        self._x_position = self.getX() + x
        self._y_position = self.getY() + y

    def attack(self):
        pass
