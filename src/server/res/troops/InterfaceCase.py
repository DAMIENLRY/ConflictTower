from abc import ABC

class InterfaceCase(ABC):
    """
    Abstract base class representing an interface for cases on the game battlefield.

    Attributes:
        _ID (int): Unique identifier for the case.
        _NAME (str): Name of the case.
        _x_position (int): X-coordinate of the case's current position.
        _y_position (int): Y-coordinate of the case's current position.
        _x_prev_position (int): X-coordinate of the case's previous position.
        _y_prev_position (int): Y-coordinate of the case's previous position.
    """

    _ID: int
    _NAME: str
    _x_position: int
    _y_position: int
    _x_prev_position: int
    _y_prev_position: int
    
    def __init__(self, x: int = 0, y: int = 0) -> None:
        super().__init__()
        self._x_position = x
        self._y_position = y
        self._x_prev_position = None
        self._y_prev_position = None
        
    
    def get_id(self) -> int:
        """
        Get the unique identifier of the case.

        Returns:
            int: The case's unique identifier.
        """
        return self._ID
    
    def get_name(self) -> str:
        """
        Get the name of the case.

        Returns:
            str: The name of the case.
        """
        return self._NAME
    
    def get_x(self) -> int:
        """
        Get the X-coordinate of the case's current position.

        Returns:
            int: The X-coordinate of the case's current position.
        """
        return self._x_position

    def get_y(self) -> int:
        """
        Get the Y-coordinate of the case's current position.

        Returns:
            int: The Y-coordinate of the case's current position.
        """
        return self._y_position
    
    def get_previous_x(self) -> int:
        """
        Get the X-coordinate of the case's previous position.

        Returns:
            int: The X-coordinate of the case's previous position.
        """
        return self._x_prev_position

    def get_previous_y(self) -> int:
        """
        Get the Y-coordinate of the case's previous position.

        Returns:
            int: The Y-coordinate of the case's previous position.
        """
        return self._y_prev_position
