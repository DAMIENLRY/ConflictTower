from enum import Enum
import j2l.pytactx.agent as pytactx
from dotenv import load_dotenv
import os
import time
import sys

from agentTower import AgentTower

# Obtenez le chemin du répertoire parent de ConflictTower (c'est-à-dire le dossier contenant ConflictTower)
current_file = os.path.abspath(__file__)  # Chemin actuel du script en cours
parent_directory = os.path.dirname(os.path.dirname(current_file))  # Chemin du répertoire parent
sys.path.append(parent_directory)  # Ajoute le répertoire parent au chemin de recherche

# Maintenant, importez votre module
from server.res.BattleField import BattleField

from server.res.cards.enums.EnumSide import EnumSide
from server.res.cards.BallonCard import BallonCard
from server.res.cards.BowlerCard import BowlerCard
from server.res.cards.GoblinCard import GoblinCard
from server.res.cards.HogRiderCard import HogRiderCard
import api.towerFinder as tf

from globaleVariable import COLUMNS, ROWS

TOWER_SIDE_1 = [
    (4,6),
    (3,5), (3,7),
    (2,5), (2,7),
    (1,6)
]
TOWER_SIDE_2 = [
    (16,6),
    (17,5), (17,7),
    (18,5), (18,7),
    (19,6)
]


load_dotenv()
arbitrerSecret = os.getenv('arbitrerSecret')

agent = AgentTower(playerId="667VELIB",
						arena="conflicttower",
						username="demo",
						password="demo",
						server="mqtt.jusdeliens.com",
						verbosity=2)

archer = BallonCard(EnumSide.SIDE_1)
archer2 = BallonCard(EnumSide.SIDE_1)

agent.addDeckCard(archer)

agent.print()

battleField = BattleField()

def initArbitrers():
    arbitre1 = pytactx.Agent(playerId=arbitrerSecret,
                             arena="conflicttower",
                             username="demo",
                             password="demo",
                             server="mqtt.jusdeliens.com",
                             verbosity=2)
    arbitre1.moveTowards
    time.sleep(0.5)
    """
	for i in range(ROWS):
		for j in range(COLUMNS):
			if (i==0 or i==ROWS-1) or (j==0 or j==COLUMNS-1):
				map[i][j] = 1
	"""


    arbitre1.ruleArena(
        "bgImg", "https://raw.githubusercontent.com/DAMIENLRY/ConflictTower/main/background.png")
    arbitre1.ruleArena("gridColumns", COLUMNS)
    arbitre1.ruleArena("gridRows", ROWS)
    arbitre1.ruleArena("map", battleField.getMap())
    arbitre1.ruleArena("mapFriction", [0, 1, 1, 1])
    # arbitre1.ruleArena("mapImgs", ["","rgba(255,255,255,1)"])
    arbitre1.ruleArena("mapImgs", [
                       "", "", "https://raw.githubusercontent.com/DAMIENLRY/ConflictTower/main/assets/explosive-balloon.png", "https://raw.githubusercontent.com/DAMIENLRY/ConflictTower/main/assets/bowler.png", "https://raw.githubusercontent.com/DAMIENLRY/ConflictTower/main/assets/gobelin.png", "https://raw.githubusercontent.com/DAMIENLRY/ConflictTower/main/assets/hog-rider.png"])

    return arbitre1


def main():
    arbitre1 = initArbitrers()

    """    
    coords2 = tf.find((19,9),(3,7))
    coords3 = tf.find((15,7),(4,6))
    coords4 = tf.find((12,1),(1,6))
    """

    i = 0
    ballon = BallonCard(EnumSide.SIDE_1)
    if(ballon.getSide()==EnumSide.SIDE_1):
        towerCoords = TOWER_SIDE_2[0]
    else:
        towerCoords = TOWER_SIDE_1[0]
        
    coords = tf.pathToTower((ballon.getX(),ballon.getY()),towerCoords)
    """
    goblin = GoblinCard(coords2[i][0], coords2[i][1])
    bowler = BowlerCard(coords3[i][0], coords3[i][1])
    hogRider = HogRiderCard(coords4[i][0], coords4[i][1])
    """
    battleField.addTroop(ballon)

    """
    battleField.addTroop(goblin)
    battleField.addTroop(bowler)
    battleField.addTroop(hogRider)
    """
    while True:
        if i<=len(coords)-1:
            ballon.setLocation(coords[i][0], coords[i][1])

        """
        if i<=len(coords2)-1:
            goblin.setLocation(coords2[i][0], coords2[i][1])
        if i<=len(coords3)-1:
            bowler.setLocation(coords3[i][0], coords3[i][1])
        if i<=len(coords4)-1:
            hogRider.setLocation(coords4[i][0], coords4 [i][1])
        """

        battleField.onUpdateMap()
        arbitre1.ruleArena("map", battleField.getMap())
        arbitre1.update()
        i+=1
        time.sleep(0.5)


main()
