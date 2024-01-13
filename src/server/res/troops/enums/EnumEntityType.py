from enum import Enum

class EnumEntityType(Enum):
    """
    Enumeration representing different types of entities in the game.

    Attributes:
        AIR: Type for entities that can target air units.
        GROUND: Type for entities that can target ground units.
        AIR_AND_GROUND: Type for entities that can target both air and ground units.
    """

    AIR = 1
    GROUND = 2
    AIR_AND_GROUND = 3
