from abc import ABC
from .InterfaceCase import InterfaceCase

class InterfaceSort(InterfaceCase, ABC):
    
    _TRAVEL_TIME: int
    _TIME_DEPLOY: int
    _DESTINATION_X: int
    _DESTINATION_Y: int
    
    def __init__(self) -> None:
        """
        Initializes an instance of InterfaceSort.

        Args:
            x (int): X-coordinate of the case's initial position.
            y (int): Y-coordinate of the case's initial position.
        """
        super().__init__()
        self._x_prev_position = None
        self._y_prev_position = None