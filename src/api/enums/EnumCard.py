from enum import Enum
import os
import sys

current_file = os.path.abspath(__file__)
parent_directory = os.path.dirname(os.path.dirname(os.path.dirname(current_file)))
sys.path.append(parent_directory)

from cards.BallonCard import BallonCard
from cards.BowlerCard import BowlerCard
from cards.GoblinCard import GoblinCard
from cards.HogRiderCard import HogRiderCard
from cards.RoyalGiantCard import RoyalGiantCard
from cards.ArcherCard import ArcherCard
from cards.KnightCard import KnightCard
from cards.MinionCard import MinionCard

class EnumCard(Enum):
    """
    Enum class representing different card types.

    Attributes:
        BALLON (BallonCard): Ballon card type.
        BOWLER (BowlerCard): Bowler card type.
        GOBLIN (GoblinCard): Goblin card type.
        HOGRIDER (HogRiderCard): Hog Rider card type.
        ROYALEGIANT (RoyalGiantCard): Royal Giant card type.
        ARCHER (ArcherCard): Archer card type.
        KNIGHT (KnightCard): Knight card type.
        MINION (MinionCard): Minion card type.
    """
    BALLON = BallonCard
    BOWLER = BowlerCard
    GOBLIN = GoblinCard
    HOGRIDER = HogRiderCard
    ROYALEGIANT = RoyalGiantCard
    ARCHER = ArcherCard
    KNIGHT = KnightCard
    MINION = MinionCard
