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
    def set_troop_speed(new_speed: EnumEntitySpeed) -> None:
        RoyalGiantTroop._SPEED = new_speed
        
    @staticmethod
    def set_troop_range(new_range: int) -> None:
        RoyalGiantTroop._RANGE = new_range
        
    @staticmethod
    def set_troop_attack_speed(new_attack_speed: EnumEntitySpeed) -> None:
        RoyalGiantTroop._ATTAQUE_SPEED = new_attack_speed
        
    @staticmethod
    def set_troop_attack_damage(new_attack_damage: int) -> None:
        RoyalGiantTroop._ATTACK_DAMAGE = new_attack_damage
        
    @staticmethod
    def set_troop_type(new_type: EnumEntityType) -> None:
        RoyalGiantTroop._TYPE = new_type
        
    @staticmethod
    def set_troop_total_health(new_total_health: int) -> None:
        RoyalGiantTroop._HEALTH_POINT = new_total_health
        
    @staticmethod
    def set_troop_cost(new_cost: int) -> None:
        RoyalGiantTroop._COPPER_COST = new_cost
    
    @staticmethod
    def get_troop_id() -> int:
        return RoyalGiantTroop._ID
    
    @staticmethod
    def get_troop_name() -> int:
        return RoyalGiantTroop._NAME
    
    @staticmethod
    def get_troop_speed() -> int:
        return RoyalGiantTroop._SPEED.value
    
    @staticmethod
    def get_troop_range() -> int:
        return RoyalGiantTroop._RANGE
    
    @staticmethod
    def get_troop_attack_speed() -> int:
        return RoyalGiantTroop._ATTAQUE_SPEED.value
    
    @staticmethod
    def get_troop_attack_damage() -> int:
        return RoyalGiantTroop._ATTACK_DAMAGE
    
    @staticmethod
    def get_troop_type() -> int:
        return RoyalGiantTroop._TYPE.value
    
    @staticmethod
    def get_troop_total_health() -> int:
        return RoyalGiantTroop._HEALTH_POINT
    
    @staticmethod
    def get_troop_cost() -> int:
        return RoyalGiantTroop._COPPER_COST
    
    @staticmethod
    def get_troop_data() -> dict:
        return {
            RoyalGiantTroop.get_troop_id(): {
                'name': RoyalGiantTroop.get_troop_name(),
                'speed': RoyalGiantTroop.get_troop_speed(),
                'range': RoyalGiantTroop.get_troop_range(),
                'attack_speed': RoyalGiantTroop.get_troop_attack_speed(),
                'attack_damage': RoyalGiantTroop.get_troop_attack_damage(),
                'type': RoyalGiantTroop.get_troop_type(),
                'total_health': RoyalGiantTroop.get_troop_total_health(),
                'cost': RoyalGiantTroop.get_troop_cost()
            }
        }
