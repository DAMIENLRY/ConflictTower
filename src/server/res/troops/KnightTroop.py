from res.troops.InterfaceTroop import InterfaceTroop
from .enums.EnumEntitySpeed import EnumEntitySpeed
from .enums.EnumEntityType import EnumEntityType

class KnightTroop(InterfaceTroop):
    """
    Concrete class representing a Knight troop in the game.

    Args:
        side (int): The side or team to which the troop belongs.

    Attributes:
        _ID (int): Unique identifier for the troop.
        _NAME (str): Name of the troop.
        _SPEED (EnumEntitySpeed): Speed of the troop.
        _RANGE (int): Attack range of the troop.
        _ATTAQUE_SPEED (EnumEntitySpeed): Attack speed of the troop.
        _ATTACK_DAMAGE (int): Attack damage of the troop.
        _TYPE (EnumEntityType): Type of the troop.
        _HEALTH_POINT (int): Health points of the troop.
        _x_position (int): X-coordinate of the troop's current position.
        sition (int): Y-coordinate of the troop's current position.
        _x_prev_position (int): X-coordinate of the troop's previous position.
        _y_prev_position (int): Y-coordinate of the troop's previous position.
        _side (int): The side or team to which the troop belongs.
        _state (FocusTowerState): The state of focus on the tower.
        _battlefield (BattleField): Instance of the game battlefield.
    """
    
    _ID = 8
    _NAME = "Chevalier"
    _SPEED = EnumEntitySpeed.AVERAGE
    _RANGE = 5
    _ATTAQUE_SPEED = EnumEntitySpeed.AVERAGE
    _ATTACK_DAMAGE = 15
    _TYPE = EnumEntityType.GROUND
    _HEALTH_POINT = 100
    _COPPER_COST = 30
        
    def __init__(self, side: int, x: int = 0, y: int = 0) -> None:
        super().__init__(side, x, y)
    
    @staticmethod
    def get_troop_id() -> int:
        return KnightTroop._ID
    
    @staticmethod
    def get_troop_cost() -> int:
        return KnightTroop._COPPER_COST
