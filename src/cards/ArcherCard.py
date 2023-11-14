from typing import List
from cards.InterfaceCard import InterfaceCard
from cards.enums.EnumEntitySpeed import EnumEntitySpeed
from cards.enums.EnumEntityType import EnumEntityType

class ArcherCard(InterfaceCard):

    def __init__(self, x, y) -> None:
        self.ID = 1
        self.NAME = "Archer"
        self.SPEED = EnumEntitySpeed.AVERAGE
        self.RANGE = 5
        self.ATTAQUE_SPEED = EnumEntitySpeed.AVERAGE
        self.TYPE = EnumEntityType.GROUND
        self.HEALTH_POINT = 100
        self.POINT = 3
        self._x_position = x
        self._y_position = y
    


    