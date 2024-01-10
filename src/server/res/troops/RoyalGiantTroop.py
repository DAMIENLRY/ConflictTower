from .InterfaceTroop import InterfaceTroop
from .enums.EnumEntitySpeed import EnumEntitySpeed
from .enums.EnumEntityType import EnumEntityType
from .states.FocusTowerState import FocusTowerState
from res.BattleField import BattleField

class RoyalGiantTroop(InterfaceTroop):
        
    def __init__(self, side: int) -> None:
        self._ID = 6
        self._NAME = "Géant Royal"
        self._SPEED = EnumEntitySpeed['SLOW']
        self._RANGE = 5
        self._ATTAQUE_SPEED = EnumEntitySpeed['SLOW']
        self._ATTACK_DAMAGE = 20
        self._TYPE = EnumEntityType['GROUND']
        self._HEALTH_POINT = 100
        self._x_position = None
        self._y_position = None
        self._x_prev_position = None
        self._y_prev_position = None
        self._side = side
        self._battlefield = BattleField.getInstance()
