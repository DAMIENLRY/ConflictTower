from .InterfaceTroop import InterfaceTroop
from .enums.EnumEntitySpeed import EnumEntitySpeed
from .enums.EnumEntityType import EnumEntityType
from .states.FocusTowerState import FocusTowerState
from res.BattleField import BattleField

class ArcherTroop(InterfaceTroop):
    """
    Class representing an Archer troop in the game.

    Attributes:
        _ID (int): Unique identifier for the troop.
        _NAME (str): Name of the troop.
        _SPEED (EnumEntitySpeed): Speed of the troop.
        _RANGE (int): Attack range of the troop.
        _ATTAQUE_SPEED (EnumEntitySpeed): Attack speed of the troop.
        _ATTACK_DAMAGE (int): Damage inflicted by the troop's attack.
        _TYPE (EnumEntityType): Type of the troop (e.g., GROUND, AIR).
        _HEALTH_POINT (int): Health points of the troop.
        _x_position (int): X-coordinate of the troop's current position.
        _y_position (int): Y-coordinate of the troop's current position.
        _x_prev_position (int): X-coordinate of the troop's previous position.
        _y_prev_position (int): Y-coordinate of the troop's previous position.
        _side (int): Team side of the troop.
        _state (FocusTowerState): State of the troop.
        _battlefield (BattleField): Instance of the BattleField.
    """

    def __init__(self, side: int) -> None:
        """
        Initializes an ArcherTroop instance.

        Args:
            side (int): Team side of the troop.
        """
        self._ID = 7
        self._NAME = "Archer"
        self._SPEED = EnumEntitySpeed['AVERAGE']
        self._RANGE = 5
        self._ATTAQUE_SPEED = EnumEntitySpeed['AVERAGE']
        self._ATTACK_DAMAGE = 8
        self._TYPE = EnumEntityType['GROUND']
        self._HEALTH_POINT = 100
        self._x_position = None
        self._y_position = None
        self._x_prev_position = None
        self._y_prev_position = None
        self._side = side
        self._state = FocusTowerState()
        self._battlefield = BattleField.get_instance()
