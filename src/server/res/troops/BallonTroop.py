from res.troops.InterfaceTroop import InterfaceTroop
from .enums.EnumEntitySpeed import EnumEntitySpeed
from .enums.EnumEntityType import EnumEntityType

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
        lefield (BattleField): Instance of the BattleField.
    """
    
    _ID = 2
    _NAME = "Balloon"
    _SPEED = EnumEntitySpeed.LIGHT_SPEED
    _RANGE = 3
    _ATTAQUE_SPEED = EnumEntitySpeed.AVERAGE
    _ATTACK_DAMAGE = 15
    _TYPE = EnumEntityType.GROUND
    _HEALTH_POINT = 100
    _COPPER_COST = 50

    def __init__(self, side: int, x: int = 0, y: int = 0) -> None:
        """
        Initializes a BallonTroop instance.

        Args:
            side (int): Team side of the troop.
        """
        super().__init__(side, x, y)
        
    @staticmethod
    def get_troop_id() -> int:
        return BallonTroop._ID
    
    @staticmethod
    def get_troop_cost() -> int:
        return BallonTroop._COPPER_COST
