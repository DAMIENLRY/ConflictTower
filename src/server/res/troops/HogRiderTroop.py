from res.troops.InterfaceTroop import InterfaceTroop
from .enums.EnumEntitySpeed import EnumEntitySpeed
from .enums.EnumEntityType import EnumEntityType

class HogRiderTroop(InterfaceTroop):
    """
    Class representing a Hog Rider troop in the game.

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
        _side (int): Team side of the troop.
        _state (FocusTowerState): State of the troop.
        _battlefield (BattleField): Instance of the BattleField.
    """

    _ID = 5
    _NAME = "Hog Rider"
    _SPEED = EnumEntitySpeed.FAST
    _RANGE = 5
    _ATTAQUE_SPEED = EnumEntitySpeed.AVERAGE
    _ATTACK_DAMAGE = 6
    _TYPE = EnumEntityType.GROUND
    _HEALTH_POINT = 100
    _COPPER_COST = 40
    
    def __init__(self, side: int, x: int = 0, y: int = 0) -> None:
        """
        Initializes a HogRiderTroop instance.

        Args:
            side (int): Team side of the troop.
        """
        super().__init__(side, x, y)
    
    @staticmethod
    def set_troop_speed(new_speed: EnumEntitySpeed) -> None:
        """Sets the speed of the HogRiderTroop."""
        HogRiderTroop._SPEED = new_speed
        
    @staticmethod
    def set_troop_range(new_range: int) -> None:
        """Sets the attack range of the HogRiderTroop."""
        HogRiderTroop._RANGE = new_range
        
    @staticmethod
    def set_troop_attack_speed(new_attack_speed: EnumEntitySpeed) -> None:
        """Sets the attack speed of the HogRiderTroop."""
        HogRiderTroop._ATTAQUE_SPEED = new_attack_speed
        
    @staticmethod
    def set_troop_attack_damage(new_attack_damage: int) -> None:
        """Sets the attack damage of the HogRiderTroop."""
        HogRiderTroop._ATTACK_DAMAGE = new_attack_damage
        
    @staticmethod
    def set_troop_type(new_type: EnumEntityType) -> None:
        """Sets the type of the HogRiderTroop (e.g., GROUND, AIR)."""
        HogRiderTroop._TYPE = new_type
        
    @staticmethod
    def set_troop_total_health(new_total_health: int) -> None:
        """Sets the total health of the HogRiderTroop."""
        HogRiderTroop._HEALTH_POINT = new_total_health
        
    @staticmethod
    def set_troop_cost(new_cost: int) -> None:
        """Sets the cost of the HogRiderTroop in copper."""
        HogRiderTroop._COPPER_COST = new_cost
    
    @staticmethod
    def get_troop_id() -> int:
        """Gets the unique identifier of the HogRiderTroop."""
        return HogRiderTroop._ID
    
    @staticmethod
    def get_troop_name() -> int:
        """Gets the name of the HogRiderTroop."""
        return HogRiderTroop._NAME
    
    @staticmethod
    def get_troop_speed() -> int:
        """Gets the speed of the HogRiderTroop."""
        return HogRiderTroop._SPEED.value
    
    @staticmethod
    def get_troop_range() -> int:
        """Gets the attack range of the HogRiderTroop."""
        return HogRiderTroop._RANGE
    
    @staticmethod
    def get_troop_attack_speed() -> int:
        """Gets the attack speed of the HogRiderTroop."""
        return HogRiderTroop._ATTAQUE_SPEED.value
    
    @staticmethod
    def get_troop_attack_damage() -> int:
        """Gets the attack damage of the HogRiderTroop."""
        return HogRiderTroop._ATTACK_DAMAGE
    
    @staticmethod
    def get_troop_type() -> int:
        """Gets the type of the HogRiderTroop (e.g., GROUND, AIR)."""
        return HogRiderTroop._TYPE.value
    
    @staticmethod
    def get_troop_total_health() -> int:
        """Gets the total health of the HogRiderTroop."""
        return HogRiderTroop._HEALTH_POINT
    
    @staticmethod
    def get_troop_cost() -> int:
        """Gets the cost of the HogRiderTroop in copper."""
        return HogRiderTroop._COPPER_COST

    @staticmethod
    def get_troop_data() -> dict:
        """Gets a dictionary containing data about the HogRiderTroop."""
        return {
            HogRiderTroop.get_troop_id(): {
                'name': HogRiderTroop.get_troop_name(),
                'speed': HogRiderTroop.get_troop_speed(),
                'range': HogRiderTroop.get_troop_range(),
                'attack_speed': HogRiderTroop.get_troop_attack_speed(),
                'attack_damage': HogRiderTroop.get_troop_attack_damage(),
                'type': HogRiderTroop.get_troop_type(),
                'total_health': HogRiderTroop.get_troop_total_health(),
                'cost': HogRiderTroop.get_troop_cost()
            }
        }
