from res.troops.InterfaceTroop import InterfaceTroop
from .enums.EnumEntitySpeed import EnumEntitySpeed
from .enums.EnumEntityType import EnumEntityType

class MinionTroop(InterfaceTroop):
    """
    Concrete class representing a Minion troop in the game.

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
        
    _ID = 9
    _NAME = "Gargouilles"
    _SPEED = EnumEntitySpeed.AVERAGE
    _RANGE = 5
    _ATTAQUE_SPEED = EnumEntitySpeed.AVERAGE
    _ATTACK_DAMAGE = 5
    _TYPE = EnumEntityType.GROUND
    _HEALTH_POINT = 100
    _COPPER_COST = 30
    
    def __init__(self, side: int, x: int = 0, y: int = 0) -> None:
        super().__init__(side, x, y)
    
    @staticmethod
    def set_troop_speed(new_speed: EnumEntitySpeed) -> None:
        """Sets the speed of the MinionTroop."""
        MinionTroop._SPEED = new_speed
        
    @staticmethod
    def set_troop_range(new_range: int) -> None:
        """Sets the attack range of the MinionTroop."""
        MinionTroop._RANGE = new_range
        
    @staticmethod
    def set_troop_attack_speed(new_attack_speed: EnumEntitySpeed) -> None:
        """Sets the attack speed of the MinionTroop."""
        MinionTroop._ATTAQUE_SPEED = new_attack_speed
        
    @staticmethod
    def set_troop_attack_damage(new_attack_damage: int) -> None:
        """Sets the attack damage of the MinionTroop."""
        MinionTroop._ATTACK_DAMAGE = new_attack_damage
        
    @staticmethod
    def set_troop_type(new_type: EnumEntityType) -> None:
        """Sets the type of the MinionTroop (e.g., GROUND, AIR)."""
        MinionTroop._TYPE = new_type
        
    @staticmethod
    def set_troop_total_health(new_total_health: int) -> None:
        """Sets the total health of the MinionTroop."""
        MinionTroop._HEALTH_POINT = new_total_health
        
    @staticmethod
    def set_troop_cost(new_cost: int) -> None:
        """Sets the cost of the MinionTroop in copper."""
        MinionTroop._COPPER_COST = new_cost
    
    @staticmethod
    def get_troop_id() -> int:
        """Gets the ID of the MinionTroop."""
        return MinionTroop._ID
    
    @staticmethod
    def get_troop_name() -> int:
        """Gets the name of the MinionTroop."""
        return MinionTroop._NAME
    
    @staticmethod
    def get_troop_speed() -> int:
        """Gets the speed of the MinionTroop."""
        return MinionTroop._SPEED.value
    
    @staticmethod
    def get_troop_range() -> int:
        """Gets the attack range of the MinionTroop."""
        return MinionTroop._RANGE
    
    @staticmethod
    def get_troop_attack_speed() -> int:
        """Gets the attack speed of the MinionTroop."""
        return MinionTroop._ATTAQUE_SPEED.value
    
    @staticmethod
    def get_troop_attack_damage() -> int:
        """Gets the attack damage of the MinionTroop."""
        return MinionTroop._ATTACK_DAMAGE
    
    @staticmethod
    def get_troop_type() -> int:
        """Gets the type of the MinionTroop."""
        return MinionTroop._TYPE.value
    
    @staticmethod
    def get_troop_total_health() -> int:
        """Gets the total health of the MinionTroop."""
        return MinionTroop._HEALTH_POINT
    
    @staticmethod
    def get_troop_cost() -> int:
        """Gets the cost of the MinionTroop."""
        return MinionTroop._COPPER_COST
    
    @staticmethod
    def get_troop_data() -> dict:
        """Gets a dictionary containing data of the MinionTroop."""
        return {
            MinionTroop.get_troop_id(): {
                'name': MinionTroop.get_troop_name(),
                'speed': MinionTroop.get_troop_speed(),
                'range': MinionTroop.get_troop_range(),
                'attack_speed': MinionTroop.get_troop_attack_speed(),
                'attack_damage': MinionTroop.get_troop_attack_damage(),
                'type': MinionTroop.get_troop_type(),
                'total_health': MinionTroop.get_troop_total_health(),
                'cost': MinionTroop.get_troop_cost()
            }
        }
