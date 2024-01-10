from enum import Enum
import os
import sys

# Obtenez le chemin du répertoire parent de ConflictTower (c'est-à-dire le dossier contenant ConflictTower)
current_file = os.path.abspath(__file__)  # Chemin actuel du script en cours
parent_directory = os.path.dirname(os.path.dirname(os.path.dirname(current_file)))  # Chemin du répertoire parent
sys.path.append(parent_directory)  # Ajoute le répertoire parent au chemin de recherche

from cards.BallonCard import BallonCard
from cards.BowlerCard import BowlerCard
from cards.GoblinCard import GoblinCard
from cards.HogRiderCard import HogRiderCard
from cards.RoyalGiantCard import RoyalGiantCard
from cards.ArcherCard import ArcherCard
from cards.KnightCard import KnightCard
from cards.MinionCard import MinionCard

class EnumCard(Enum):
    BALLON = BallonCard
    BOWLER = BowlerCard
    GOBLIN = GoblinCard
    HOGRIDER = HogRiderCard
    ROYALEGIANT = RoyalGiantCard
    ARCHER = ArcherCard
    KNIGHT = KnightCard
    MINION = MinionCard