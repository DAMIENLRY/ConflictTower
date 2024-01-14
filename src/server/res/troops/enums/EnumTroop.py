from enum import Enum

from res.troops.BallonTroop import BallonTroop
from res.troops.BowlerTroop import BowlerTroop
from res.troops.GoblinTroop import GoblinTroop
from res.troops.HogRiderTroop import HogRiderTroop
from res.troops.RoyalGiantTroop import RoyalGiantTroop
from res.troops.ArcherTroop import ArcherTroop
from res.troops.KnightTroop import KnightTroop
from res.troops.MinionTroop import MinionTroop

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
