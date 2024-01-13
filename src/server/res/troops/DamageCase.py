from .InterfaceCase import InterfaceCase

class DamageCase(InterfaceCase):
    """
    Class representing a damage case on the game map.

    Attributes:
        _ID (int): Unique identifier for the damage case.
        _NAME (str): Name of the damage case.
        _x_position (int): X-coordinate of the damage case on the game map.
        _y_position (int): Y-coordinate of the damage case on the game map.
    """

    def __init__(self, frictionId=3, x=0, y=0) -> None:
        """
        Initializes a DamageCase instance.

        Args:
            frictionId (int): Identifier for the friction associated with the damage case.
            x (int): X-coordinate of the damage case on the game map.
            y (int): Y-coordinate of the damage case on the game map.
        """
        self._ID = int("1" + str(frictionId))
        self._NAME = 'DamageCase'
        self._x_position = x
        self._y_position = y
