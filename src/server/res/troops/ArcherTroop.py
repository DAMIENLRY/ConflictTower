from res.troops.InterfaceTroop import InterfaceTroop
from .enums.EnumEntitySpeed import EnumEntitySpeed
from .enums.EnumEntityType import EnumEntityType

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
    
    _ID = 7
    _NAME = "Archer"
    _SPEED = EnumEntitySpeed.AVERAGE
    _RANGE = 5
    _ATTAQUE_SPEED = EnumEntitySpeed.AVERAGE
    _ATTACK_DAMAGE = 8
    _TYPE = EnumEntityType.GROUND
    _HEALTH_POINT = 100
    _COPPER_COST = 20

    def __init__(self, side: int, x: int = 0, y: int = 0) -> None:
        """
        Initializes an ArcherTroop instance.

        Args:
            side (int): Team side of the troop.
        """
        super().__init__(side, x, y)
        
    @staticmethod
    def get_troop_id() -> int:
        return ArcherTroop._ID
    
    @staticmethod
    def get_troop_cost() -> int:
        return ArcherTroop._COPPER_COST
