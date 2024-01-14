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
    def set_troop_speed(new_speed: EnumEntitySpeed) -> None:
        BallonTroop._SPEED = new_speed
        
    @staticmethod
    def set_troop_range(new_range: int) -> None:
        BallonTroop._RANGE = new_range
        
    @staticmethod
    def set_troop_attack_speed(new_attack_speed: EnumEntitySpeed) -> None:
        BallonTroop._ATTAQUE_SPEED = new_attack_speed
        
    @staticmethod
    def set_troop_attack_damage(new_attack_damage: int) -> None:
        BallonTroop._ATTACK_DAMAGE = new_attack_damage
        
    @staticmethod
    def set_troop_type(new_type: EnumEntityType) -> None:
        BallonTroop._TYPE = new_type
        
    @staticmethod
    def set_troop_total_health(new_total_health: int) -> None:
        BallonTroop._HEALTH_POINT = new_total_health
        
    @staticmethod
    def set_troop_cost(new_cost: int) -> None:
        BallonTroop._COPPER_COST = new_cost
        
    @staticmethod
    def get_troop_id() -> int:
        return BallonTroop._ID
    
    @staticmethod
    def get_troop_name() -> int:
        return BallonTroop._NAME
    
    @staticmethod
    def get_troop_speed() -> int:
        return BallonTroop._SPEED.value
    
    @staticmethod
    def get_troop_range() -> int:
        return BallonTroop._RANGE
    
    @staticmethod
    def get_troop_attack_speed() -> int:
        return BallonTroop._ATTAQUE_SPEED.value
    
    @staticmethod
    def get_troop_attack_damage() -> int:
        return BallonTroop._ATTACK_DAMAGE
    
    @staticmethod
    def get_troop_type() -> int:
        return BallonTroop._TYPE.value
    
    @staticmethod
    def get_troop_total_health() -> int:
        return BallonTroop._HEALTH_POINT
    
    @staticmethod
    def get_troop_cost() -> int:
        return BallonTroop._COPPER_COST
    
    @staticmethod
    def get_troop_data() -> dict:
        return {
            BallonTroop.get_troop_id(): {
                'name': BallonTroop.get_troop_name(),
                'speed': BallonTroop.get_troop_speed(),
                'range': BallonTroop.get_troop_range(),
                'attack_speed': BallonTroop.get_troop_attack_speed(),
                'attack_damage': BallonTroop.get_troop_attack_damage(),
                'type': BallonTroop.get_troop_type(),
                'total_health': BallonTroop.get_troop_total_health(),
                'cost': BallonTroop.get_troop_cost()
            }
        }
