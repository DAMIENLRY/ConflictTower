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
        _y_position (int): Y-coordinate of the troop's current position.
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
    def set_troop_speed(new_speed: EnumEntitySpeed) -> None:
        """Sets the speed of the KnightTroop."""
        KnightTroop._SPEED = new_speed
        
    @staticmethod
    def set_troop_range(new_range: int) -> None:
        """Sets the attack range of the KnightTroop."""
        KnightTroop._RANGE = new_range
        
    @staticmethod
    def set_troop_attack_speed(new_attack_speed: EnumEntitySpeed) -> None:
        """Sets the attack speed of the KnightTroop."""
        KnightTroop._ATTAQUE_SPEED = new_attack_speed
        
    @staticmethod
    def set_troop_attack_damage(new_attack_damage: int) -> None:
        """Sets the attack damage of the KnightTroop."""
        KnightTroop._ATTACK_DAMAGE = new_attack_damage
        
    @staticmethod
    def set_troop_type(new_type: EnumEntityType) -> None:
        """Sets the type of the KnightTroop (e.g., GROUND, AIR)."""
        KnightTroop._TYPE = new_type
        
    @staticmethod
    def set_troop_total_health(new_total_health: int) -> None:
        """Sets the total health of the KnightTroop."""
        KnightTroop._HEALTH_POINT = new_total_health
        
    @staticmethod
    def set_troop_cost(new_cost: int) -> None:
        """Sets the cost of the KnightTroop in copper."""
        KnightTroop._COPPER_COST = new_cost
    
    @staticmethod
    def get_troop_id() -> int:
        """Gets the ID of the KnightTroop."""
        return KnightTroop._ID
    
    @staticmethod
    def get_troop_name() -> int:
        """Gets the name of the KnightTroop."""
        return KnightTroop._NAME
    
    @staticmethod
    def get_troop_speed() -> int:
        """Gets the speed of the KnightTroop."""
        return KnightTroop._SPEED.value
    
    @staticmethod
    def get_troop_range() -> int:
        """Gets the attack range of the KnightTroop."""
        return KnightTroop._RANGE
    
    @staticmethod
    def get_troop_attack_speed() -> int:
        """Gets the attack speed of the KnightTroop."""
        return KnightTroop._ATTAQUE_SPEED.value
    
    @staticmethod
    def get_troop_attack_damage() -> int:
        """Gets the attack damage of the KnightTroop."""
        return KnightTroop._ATTACK_DAMAGE
    
    @staticmethod
    def get_troop_type() -> int:
        """Gets the type of the KnightTroop."""
        return KnightTroop._TYPE.value
    
    @staticmethod
    def get_troop_total_health() -> int:
        """Gets the total health of the KnightTroop."""
        return KnightTroop._HEALTH_POINT
    
    @staticmethod
    def get_troop_cost() -> int:
        """Gets the cost of the KnightTroop."""
        return KnightTroop._COPPER_COST
    
    @staticmethod
    def get_troop_data() -> dict:
        """Gets a dictionary containing data of the KnightTroop."""
        return {
            KnightTroop.get_troop_id(): {
                'name': KnightTroop.get_troop_name(),
                'speed': KnightTroop.get_troop_speed(),
                'range': KnightTroop.get_troop_range(),
                'attack_speed': KnightTroop.get_troop_attack_speed(),
                'attack_damage': KnightTroop.get_troop_attack_damage(),
                'type': KnightTroop.get_troop_type(),
                'total_health': KnightTroop.get_troop_total_health(),
                'cost': KnightTroop.get_troop_cost()
            }
        }
