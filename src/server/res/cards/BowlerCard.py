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
        self._ATTACK_DAMAGE = 10
        self._TYPE = EnumEntityType['GROUND']
        self._HEALTH_POINT = 30
        self._x_position = x
        self._y_position = y
        self._x_prev_position = None
        self._y_prev_position = None
        self._battlefield = BattleField.getInstance()