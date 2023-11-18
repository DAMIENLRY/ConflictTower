from .InterfaceCard import InterfaceCard
from .enums.EnumEntitySpeed import EnumEntitySpeed
from .enums.EnumEntityType import EnumEntityType
from .enums.EnumSide import EnumSide
from server.res.BattleField import BattleField
from server.res.cards.states.FocusTowerState import FocusTowerState

from api.globaleVariable import COLUMNS, ROWS

class BowlerCard(InterfaceCard):

    def __init__(self, side: EnumSide,x,y) -> None:
        self._ID = 3
        self._NAME = "Bouliste"
        self._SPEED = EnumEntitySpeed['FAST']
        self._state = FocusTowerState()
        self._side = side
        self._RANGE = 2
        self._ATTAQUE_SPEED = EnumEntitySpeed['AVERAGE']
        self._TYPE = EnumEntityType['GROUND']
        self._HEALTH_POINT = 100
        self._x_position = x
        self._y_position = y
        self._x_prev_position = None
        self._y_prev_position = None
        self._battlefield = BattleField.getInstance()


    def setLocation(self, x: int, y: int):
        if x>=1 and x<=ROWS-1 and y>=0 and y<=COLUMNS-1:
            if self._x_position and self._y_position:
                self._x_prev_position = self._x_position
                self._y_prev_position = self._y_position
            self._x_position = x
            self._y_position = y
            BattleField.getInstance().onUpdateMap()
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