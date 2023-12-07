from .InterfaceCard import InterfaceCard
from .enums.EnumEntitySpeed import EnumEntitySpeed
from .enums.EnumEntityType import EnumEntityType
from .enums.EnumSide import EnumSide
from server.res.BattleField import BattleField

from api.globaleVariable import COLUMNS, ROWS

class GoblinCard(InterfaceCard):
        
    def __init__(self, side: EnumSide) -> None:
        self._ID = 4
        self._NAME = "Gobelin"
        self._SPEED = EnumEntitySpeed['AVERAGE']
        self._RANGE = 5
        self._ATTAQUE_SPEED = EnumEntitySpeed['AVERAGE']
        self._ATTACK_DAMAGE = 5
        self._TYPE = EnumEntityType['GROUND']
        self._HEALTH_POINT = 100
        self._x_position = None
        self._y_position = None
        self._x_prev_position = None
        self._y_prev_position = None
        self._side = side
        self._battlefield = BattleField.getInstance()


    def setLocation(self, x: int, y: int):
        if x>=1 and x<=ROWS-1 and y>=0 and y<=COLUMNS-1:
            if self._x_position and self._y_position:
                self._x_prev_position = self._x_position
                self._y_prev_position = self._y_position
            self._x_position = x
            self._y_position = y
        else:
            return False
