from abc import ABC, abstractmethod
from cards.enums.EnumEntitySpeed import EnumEntitySpeed
from cards.enums.EnumEntityType import EnumEntityType

class InterfaceCard(ABC):

    ID: int
    NAME: str
    SPEED: EnumEntitySpeed
    RANGE: float
    ATTAQUE_SPEED: EnumEntitySpeed
    TYPE: EnumEntityType
    HEALTH_POINT: int
    POINT: int
    _x_position: int
    _y_position: int

    def __init__(self, x, y) -> None:
        self._x_position = x
        self._y_position = y

    @property
    def getX(self) -> int:
        return self._x_position
    
    @property
    def getY(self) -> int:
        return self._y_position


    
    
    