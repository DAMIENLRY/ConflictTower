from abc import ABC

class InterfaceCase(ABC):
    
    _ID: int
    _NAME: str
    _x_position: int
    _y_position: int
    _x_prev_position: int
    _y_prev_position: int
    
    def get_id(self) -> int:
        return self._ID
    
    def get_name(self) -> str:
        return self._NAME
    
    def get_x(self) -> int:
        return self._x_position

    def get_y(self) -> int:
        return self._y_position
    
    def get_previous_x(self) -> int:
        return self._x_prev_position

    def get_previous_y(self) -> int:
        return self._y_prev_position
