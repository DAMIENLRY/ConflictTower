from .InterfaceCase import InterfaceCase


class ObstacleCase(InterfaceCase):
    
    def __init__(self, x, y):
        self._ID = 1
        self._NAME = 'ObstacleCase'
        self._x_position = x
        self._y_position = y