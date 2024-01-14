from res.troops.InterfaceTroop import InterfaceTroop
from .enums.EnumEntitySpeed import EnumEntitySpeed
from .enums.EnumEntityType import EnumEntityType

class RoyalGiantTroop(InterfaceTroop):
    """
    Concrete class representing the Royal Giant troop in the game.

    Args:
        side (int): Side or team to which the Royal Giant belongs.

    Attributes:
        _ID (int): Unique identifier for the troop.
        _NAME (str): Name of the troop.
        _SPEED (EnumEntitySpeed): Speed of the troop.
        _RANGE (int): Attack range of the troop.
        _ATTAQUE_SPEED (EnumEntitySpeed): Attack speed of the troop.
        _ATTACK_DAMAGE (int): Damage dealt by the troop's attack.
        _TYPE (EnumEntityType): Type of the troop.
        _HEALTH_POINT (int): Health points of the troop.
        _x_position (int): X-coordinate of the troop's current position.
        _y_position (int): Y-coordinate of the troop's current position.
        _x_prev_position (int): X-coordinate of the troop's previous position.
        _y_prev_position (int): Y-coordinate of the troop's previous position.
        _side (int): Side or team to which the Royal Giant belongs.
        _state (FocusTowerState): State representing the focus on a tower.
        _battlefield (BattleField): Reference to the game's battlefield.
    """
    
    _ID = 6
    _NAME = "Géant Royal"
    _SPEED = EnumEntitySpeed.SLOW
    _RANGE = 1
    _ATTAQUE_SPEED = EnumEntitySpeed.SLOW
    _ATTACK_DAMAGE = 20
    _TYPE = EnumEntityType.GROUND
    _HEALTH_POINT = 100
    _COPPER_COST = 70
        
    def __init__(self, side: int, x: int = 0, y: int = 0) -> None:
        super().__init__(side, x, y)
    
    @staticmethod
    def get_troop_id() -> int:
        return RoyalGiantTroop._ID
    
    @staticmethod
    def get_troop_cost() -> int:
        return RoyalGiantTroop._COPPER_COST
