from .InterfaceCard import InterfaceCard
from .enums.EnumEntitySpeed import EnumEntitySpeed
from .enums.EnumEntityType import EnumEntityType
from .enums.EnumSide import EnumSide
from server.res.BattleField import BattleField
from server.res.cards.states.FocusTowerState import FocusTowerState

from api.globaleVariable import COLUMNS, ROWS

class BowlerCard(InterfaceCard):

    def __init__(self, side: EnumSide) -> None:
        self._ID = 3
        self._NAME = "Bouliste"
        self._SPEED = EnumEntitySpeed['LIGHT_SPEED']
        self._state = FocusTowerState()
        self._side = side
        self._RANGE = 3
        self._ATTAQUE_SPEED = EnumEntitySpeed['AVERAGE']
        self._ATTACK_DAMAGE = 10
        self._TYPE = EnumEntityType['GROUND']
        self._HEALTH_POINT = 100
        self._COPPER_COST = 40
        self._x_position = None
        self._y_position = None
        self._x_prev_position = None
        self._y_prev_position = None
        self._side = side
        self._battlefield = BattleField.getInstance()
