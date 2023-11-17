from .InterfaceCard import InterfaceCard
from .enums.EnumEntitySpeed import EnumEntitySpeed
from .enums.EnumEntityType import EnumEntityType
from .enums.EnumSide import EnumSide
from server.res.BattleField import BattleField

from api.globaleVariable import COLUMNS, ROWS

class BowlerCard(InterfaceCard):

    def __init__(self, side: EnumSide) -> None:
        self._ID = 3
        self._NAME = "Bouliste"
        self._SPEED = EnumEntitySpeed['AVERAGE']
        self._side = side
        self._RANGE = 1
        self._ATTAQUE_SPEED = EnumEntitySpeed['AVERAGE']
        self._TYPE = EnumEntityType['GROUND']
        self._HEALTH_POINT = 100
        self._x_position = 4
        self._y_position = 4
        self._x_prev_position = None
        self._y_prev_position = None
        self._battlefield = BattleField()


    def setLocation(self, x: int, y: int):
        if x>=1 and x<=ROWS-1 and y>=0 and y<=COLUMNS-1:
            if self._x_position and self._y_position:
                self._x_prev_position = self._x_position
                self._y_prev_position = self._y_position
            self._x_position = x
            self._y_position = y
        else:
            return False

    def opponentInRange(self):
        offsets = [
            (-1, -1), (-1, 0), (-1, 1),  # Top row (left, center, right)
            (0, -1),           (0, 1),   # Middle row (left, right)
            (1, -1), (1, 0), (1, 1)]     # Bottom row (left, center, right)

        for dx, dy in offsets:
            x = self._x_position + dx
            y = self._y_position + dy
                    
            targetX, targetY = dx+self._x_position, dy+self._y_position

            if(self.isWithinBounds(targetX, targetY)):
                opponent = self._battlefield.isOccupiedByOpponent(targetX, targetY)
                if opponent is not False:
                    print(opponent)
                else:
                    print("False")