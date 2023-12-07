import sys
import os

current_file = os.path.abspath(__file__)  # Chemin actuel du script en cours
parent_directory = os.path.dirname(current_file)  # Chemin du répertoire parent du parent du parent
sys.path.append(parent_directory)  # Ajoute le répertoire parent au chemin de recherche

from server.res.cards.InterfaceCase import InterfaceCase

class DamageCase(InterfaceCase):
    
    def __init__(self, frictionId=3, x=0, y=0):
        self._ID = int("1"+str(frictionId))
        self._NAME = 'DamageCase'
        self._x_position = x
        self._y_position = y