from enum import Enum
import os
import sys

# Obtenez le chemin du répertoire parent de ConflictTower (c'est-à-dire le dossier contenant ConflictTower)
current_file = os.path.abspath(__file__)  # Chemin actuel du script en cours
parent_directory = os.path.dirname(os.path.dirname(os.path.dirname(current_file)))  # Chemin du répertoire parent
sys.path.append(parent_directory)  # Ajoute le répertoire parent au chemin de recherche

from server.res.cards.BallonCard import BallonCard
from server.res.cards.BowlerCard import BowlerCard
from server.res.cards.GoblinCard import GoblinCard
from server.res.cards.HogRiderCard import HogRiderCard
from server.res.cards.RoyalGiantCard import RoyalGiantCard
from server.res.cards.ArcherCard import ArcherCard
from server.res.cards.KnightCard import KnightCard
from server.res.cards.MinionCard import MinionCard


class TroopEnum(Enum):
    BALLON = BallonCard
    BOWLER = BowlerCard
    GOBLIN = GoblinCard
    HOGRIDER = HogRiderCard
    ROYALEGIANT = RoyalGiantCard
    ARCHER = ArcherCard
    KNIGHT = KnightCard
    MINION = MinionCard
    