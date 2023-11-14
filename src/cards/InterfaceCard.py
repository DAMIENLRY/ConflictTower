from cards.enums.EnumEntitySpeed import EnumEntitySpeed
from cards.enums.EnumEntityType import EnumEntityType
from cards.states.StateCard import StateCard
from abc import ABC, abstractmethod
from cards.states.StateCard import StateCard
from cards.enums.EnumEntitySpeed import EnumEntitySpeed
from cards.enums.EnumEntityType import EnumEntityType
import time


class InterfaceCard(StateCard, ABC):

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
    _state: StateCard

    def __init__(self, x, y) -> None:
        self._x_position = x
        self._y_position = y

    @property
    def getX(self) -> int:
        return self._x_position

    @property
    def getY(self) -> int:
        return self._y_position

    @property
    def getState(self) -> StateCard:
        return self._state

    @_state.setter
    def setState(self, state) -> StateCard:
        self._state = state

    def move(self, x: int, y: int) -> None:
        if x < -1 or x > 1 or y < -1 or y > 1:
            return
        if self.SPEED == EnumEntitySpeed["SLOW"]:
            time.sleep(2)
        if self.SPEED == EnumEntitySpeed["AVERAGE"]:
            time.sleep(1)
        if self.SPEED == EnumEntitySpeed["FAST"]:
            time.sleep(0.5)
        self._x_position = self.getX() + x
        self._y_position = self.getY() + y

    def attack(self):
        pass
