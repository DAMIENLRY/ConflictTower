from .InterfaceCase import InterfaceCase


class EmptyCase(InterfaceCase):
    
    def __init__(self, x, y):
        self._ID = 0
        self._NAME = 'EmptyCase'
        self._x_position = x
        self._y_position = y