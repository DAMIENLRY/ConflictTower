from .InterfaceCase import InterfaceCase

class DamageCase(InterfaceCase):
    
    def __init__(self, frictionId=3, x=0, y=0):
        self._ID = int("1"+str(frictionId))
        self._NAME = 'DamageCase'
        self._x_position = x
        self._y_position = y