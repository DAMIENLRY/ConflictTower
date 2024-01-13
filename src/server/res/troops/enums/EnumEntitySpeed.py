from enum import Enum

class EnumEntitySpeed(Enum):
    """
    Enumeration representing different speeds for entities in the game.

    Attributes:
        SLOW: Speed value for slow entities.
        AVERAGE: Speed value for average entities.
        FAST: Speed value for fast entities.
        LIGHT_SPEED: Speed value for entities with light speed.
    """

    SLOW = 3
    AVERAGE = 1.5
    FAST = 1
    LIGHT_SPEED = 0.5
