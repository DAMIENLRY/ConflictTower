import time
from .InterfaceCard import InterfaceCard
from .enums.EnumEntitySpeed import EnumEntitySpeed
from .enums.EnumEntityType import EnumEntityType
from .enums.EnumSide import EnumSide

from server.res.cards.states.FocusTowerState import FocusTowerState
from server.res.BattleField import BattleField

from api.globaleVariable import COLUMNS, ROWS


class BallonCard(InterfaceCard):

    def __init__(self, side: EnumSide) -> None:
        self._ID = 2
        self._NAME = "Gobelin"
        self._SPEED = EnumEntitySpeed['FAST']
        self._side = side
        self._state = FocusTowerState()
        self._RANGE = 0
        self._ATTAQUE_SPEED = EnumEntitySpeed['AVERAGE']
        self._TYPE = EnumEntityType['GROUND']
        self._HEALTH_POINT = 100
        self._x_position = None
        self._y_position = None
        self._x_prev_position = None
        self._y_prev_position = None
        self._battlefield = BattleField.getInstance()