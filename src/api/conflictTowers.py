import j2l.pytactx.agent as pytactx
from dotenv import load_dotenv
import os
import time
import sys

# Obtenez le chemin du répertoire parent de ConflictTower (c'est-à-dire le dossier contenant ConflictTower)
current_file = os.path.abspath(__file__)  # Chemin actuel du script en cours
parent_directory = os.path.dirname(os.path.dirname(current_file))  # Chemin du répertoire parent
sys.path.append(parent_directory)  # Ajoute le répertoire parent au chemin de recherche

# Maintenant, importez votre module
from server.res.BattleField import BattleField
from server.res.cards.ArcherCard import ArcherCard

from globaleVariable import COLUMNS, ROWS

load_dotenv()
arbitrerSecret = os.getenv('arbitrerSecret')

"""agent = pytactx.Agent(playerId="667VELIB",
						arena="conflicttower",
						username="demo",
						password="demo",
						server="mqtt.jusdeliens.com",
						verbosity=2)"""


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
 
    battleField = BattleField()
    
    archer = ArcherCard(8, 4)
    
    battleField.addTroop(archer)
    battleField.onUpdateMap()
    
    print(battleField.getMap())

    
    arbitre1.ruleArena(
        "bgImg", "https://raw.githubusercontent.com/DAMIENLRY/ConflictTower/main/background.png")
    arbitre1.ruleArena("gridColumns", COLUMNS)
    arbitre1.ruleArena("gridRows", ROWS)
    arbitre1.ruleArena("map", battleField.getMap())
    arbitre1.ruleArena("mapFriction", [0, 1, 1, 1])
    # arbitre1.ruleArena("mapImgs", ["","rgba(255,255,255,1)"])
    arbitre1.ruleArena("mapImgs", [
                       "", "", "https://raw.githubusercontent.com/DAMIENLRY/ConflictTower/main/assets/explosive-balloon.png"])

    return arbitre1


def main():
    arbitre1 = initArbitrers()

    while True:
        arbitre1.update()
        continue


main()
