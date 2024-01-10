from enum import Enum
import os
import sys

# Obtenez le chemin du répertoire parent de ConflictTower (c'est-à-dire le dossier contenant ConflictTower)
current_file = os.path.abspath(__file__)  # Chemin actuel du script en cours
parent_directory = os.path.dirname(os.path.dirname(os.path.dirname(current_file)))  # Chemin du répertoire parent
sys.path.append(parent_directory)  # Ajoute le répertoire parent au chemin de recherche

from troops.BallonTroop import BallonTroop
from troops.BowlerTroop import BowlerTroop
from troops.GoblinTroop import GoblinTroop
from troops.HogRiderTroop import HogRiderTroop
from troops.RoyalGiantTroop import RoyalGiantTroop
from troops.ArcherTroop import ArcherTroop
from troops.KnightTroop import KnightTroop
from troops.MinionTroop import MinionTroop

class EnumTroop(Enum):
    BALLON = BallonTroop
    BOWLER = BowlerTroop
    GOBLIN = GoblinTroop
    HOGRIDER = HogRiderTroop
    ROYALEGIANT = RoyalGiantTroop
    ARCHER = ArcherTroop
    KNIGHT = KnightTroop
    MINION = MinionTroop
    