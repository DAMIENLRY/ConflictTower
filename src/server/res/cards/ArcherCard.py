from .InterfaceCard import InterfaceCard
from .enums.EnumEntitySpeed import EnumEntitySpeed
from .enums.EnumEntityType import EnumEntityType

from api.globaleVariable import COLUMNS, ROWS
from server.res.BattleField import BattleField

class ArcherCard(InterfaceCard):
        
    def __init__(self, x: int, y: int) -> None:
        self._ID = 2
        self._NAME = "Archer"
        self._SPEED = EnumEntitySpeed['AVERAGE']
        self._RANGE = 5
        self._ATTAQUE_SPEED = EnumEntitySpeed['AVERAGE']
        self._TYPE = EnumEntityType['GROUND']
        self._HEALTH_POINT = 100
        self._x_position = x
        self._y_position = y
        self._x_prev_position = x
        self._y_prev_position = y
        #self.battleField = BattleField()


    def setLocation(self, x: int, y: int):
        if x>=1 and x<=ROWS-1 and y>=0 and y<=COLUMNS-1:
            if self._x_position and self._y_position:
                self._x_prev_position = self._x_position
                self._y_prev_position = self._y_position
            self._x_position = x
            self._y_position = y
        else:
            return False
