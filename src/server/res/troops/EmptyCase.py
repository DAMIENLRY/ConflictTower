from .InterfaceCase import InterfaceCase

class EmptyCase(InterfaceCase):
    """
    Class representing an empty case on the game map.

    Attributes:
        _ID (int): Unique identifier for the empty case.
        _NAME (str): Name of the empty case.
        _x_position (int): X-coordinate of the empty case on the game map.
        _y_position (int): Y-coordinate of the empty case on the game map.
    """

    def __init__(self, x=0, y=0) -> None:
        """
        Initializes an EmptyCase instance.

        Args:
            x (int): X-coordinate of the empty case on the game map.
            y (int): Y-coordinate of the empty case on the game map.
        """
        self._ID = 0
        self._NAME = 'EmptyCase'
        self._x_position = x
        self._y_position = y