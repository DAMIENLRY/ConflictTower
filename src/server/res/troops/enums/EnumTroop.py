from enum import Enum
import os
import sys

current_file = os.path.abspath(__file__)
parent_directory = os.path.dirname(os.path.dirname(os.path.dirname(current_file)))
sys.path.append(parent_directory)

from troops.BallonTroop import BallonTroop
from troops.BowlerTroop import BowlerTroop
from troops.GoblinTroop import GoblinTroop
from troops.HogRiderTroop import HogRiderTroop
from troops.RoyalGiantTroop import RoyalGiantTroop
from troops.ArcherTroop import ArcherTroop
from troops.KnightTroop import KnightTroop
from troops.MinionTroop import MinionTroop

class EnumTroop(Enum):
    """
    Enumeration representing different troop types in the game.

    Attributes:
        BALLON: BallonTroop class.
        BOWLER: BowlerTroop class.
        GOBLIN: GoblinTroop class.
        HOGRIDER: HogRiderTroop class.
        ROYALEGIANT: RoyalGiantTroop class.
        ARCHER: ArcherTroop class.
        KNIGHT: KnightTroop class.
        MINION: MinionTroop class.
    """

    BALLON = BallonTroop
    BOWLER = BowlerTroop
    GOBLIN = GoblinTroop
    HOGRIDER = HogRiderTroop
    ROYALEGIANT = RoyalGiantTroop
    ARCHER = ArcherTroop
    KNIGHT = KnightTroop
    MINION = MinionTroop
