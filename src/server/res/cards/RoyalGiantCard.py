from .InterfaceCard import InterfaceCard
from .enums.EnumEntitySpeed import EnumEntitySpeed
from .enums.EnumEntityType import EnumEntityType

from api.globaleVariable import COLUMNS, ROWS

class RoyalGiantCard(InterfaceCard):
        
    def __init__(self) -> None:
        self._ID = 6
        self._NAME = "Géant Royal"
        self._SPEED = EnumEntitySpeed['SLOW']
        self._RANGE = 5
        self._ATTAQUE_SPEED = EnumEntitySpeed['SLOW']
        self._ATTACK_DAMAGE = 20
        self._TYPE = EnumEntityType['GROUND']
        self._HEALTH_POINT = 100
        self._x_position = 1
        self._y_position = 1

    def setLocation(self, x: int, y: int):
        if x>=1 and x<=ROWS-1 and y>=0 and y<=COLUMNS-1:
            if self._x_position and self._y_position:
                self._x_prev_position = self._x_position
                self._y_prev_position = self._y_position
            self._x_position = x
            self._y_position = y
        else:
            return False
