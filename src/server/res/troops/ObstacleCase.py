from .InterfaceCase import InterfaceCase

class ObstacleCase(InterfaceCase):
    """
    Concrete class representing an obstacle case in the game.

    Args:
        x (int): X-coordinate of the obstacle case.
        y (int): Y-coordinate of the obstacle case.

    Attributes:
        _ID (int): Unique identifier for the case.
        _NAME (str): Name of the case.
        _x_position (int): X-coordinate of the obstacle case.
        _y_position (int): Y-coordinate of the obstacle case.
    """
    
    def __init__(self, x, y):
        self._ID = 1
        self._NAME = 'ObstacleCase'
        self._x_position = x
        self._y_position = y
