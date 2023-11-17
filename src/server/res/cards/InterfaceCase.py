from abc import ABC


class InterfaceCase(ABC):
    
    _ID: int
    _NAME: str
    _x_position: int
    _y_position: int
    _x_prev_position: int
    _y_prev_position: int
    
    def getId(self) -> int:
        return self._ID
    
    def getName(self) -> str:
        return self._NAME
    
    def getX(self) -> int:
        return self._x_position

    def getY(self) -> int:
        return self._y_position
    
    def getPreviousX(self) -> int:
        return self._x_prev_position

    def getPreviousY(self) -> int:
        return self._y_prev_position
