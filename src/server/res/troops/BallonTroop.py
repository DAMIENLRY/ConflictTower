from res.troops.InterfaceTroop import InterfaceTroop
from .enums.EnumEntitySpeed import EnumEntitySpeed
from .enums.EnumEntityType import EnumEntityType
from .states.FocusTowerState import FocusTowerState
from res.BattleField import BattleField

class BallonTroop(InterfaceTroop):
    """
    Class representing a Balloon troop in the game.

    Attributes:
        _ID (int): Unique identifier for the troop.
        _NAME (str): Name of the troop.
        _SPEED (EnumEntitySpeed): Speed of the troop.
        _RANGE (int): Attack range of the troop.
        _ATTAQUE_SPEED (EnumEntitySpeed): Attack speed of the troop.
        _ATTACK_DAMAGE (int): Damage inflicted by the troop's attack.
        _TYPE (EnumEntityType): Type of the troop (e.g., GROUND, AIR).
        _HEALTH_POINT (int): Health points of the troop.
        _COPPER_COST (int): Cost of deploying the troop.
        _x_position (int): X-coordinate of the troop's current position.
        _y_position (int): Y-coordinate of the troop's current position.
        _x_prev_position (int): X-coordinate of the troop's previous position.
        _y_prev_position (int): Y-coordinate of the troop's previous position.
        _state (FocusTowerState): State of the troop.
        _battlefield (BattleField): Instance of the BattleField.
    """

    def __init__(self, side: int) -> None:
        """
        Initializes a BallonTroop instance.

        Args:
            side (int): Team side of the troop.
        """
        self._ID = 2
        self._NAME = "Balloon"
        self._SPEED = EnumEntitySpeed['LIGHT_SPEED']
        self._side = side
        self._state = FocusTowerState()
        self._RANGE = 3
        self._ATTAQUE_SPEED = EnumEntitySpeed['AVERAGE']
        self._ATTACK_DAMAGE = 15
        self._TYPE = EnumEntityType['GROUND']
        self._HEALTH_POINT = 100
        self._COPPER_COST = 50
        self._x_position = None
        self._y_position = None
        self._x_prev_position = None
        self._y_prev_position = None
        self._battlefield = BattleField.get_instance()
