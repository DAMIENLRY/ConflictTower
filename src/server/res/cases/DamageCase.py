import sys
import os

current_file = os.path.abspath(__file__)  # Chemin actuel du script en cours
parent_directory = os.path.dirname(current_file)  # Chemin du répertoire parent du parent du parent
sys.path.append(parent_directory)  # Ajoute le répertoire parent au chemin de recherche

from server.res.cards.InterfaceCase import InterfaceCase

class DamageCase(InterfaceCase):
    
    def __init__(self, x, y):
        self._ID = 6
        self._NAME = 'DamageCase'
        self._x_position = x
        self._y_position = y