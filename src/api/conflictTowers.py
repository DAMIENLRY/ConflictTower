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

from server.res.BattleField import BattleField

from server.res.cards.enums.EnumSide import EnumSide
from server.res.cards.BallonCard import BallonCard
from server.res.cards.BowlerCard import BowlerCard
from server.res.cards.GoblinCard import GoblinCard
from server.res.cards.HogRiderCard import HogRiderCard
from api.enums.TroopEnum import TroopEnum
import api.towerFinder as tf


from globaleVariable import COLUMNS, ROWS

load_dotenv()
arbitrerSecret = os.getenv('arbitrerSecret')

agent = AgentTower(playerId="667VELIB",
						arena="conflicttower",
						username="demo",
						password="demo",
						server="mqtt.jusdeliens.com",
						verbosity=2)


"""
agent.addDeckCard(TroopEnum.BALLON)
agent.addDeckCard(TroopEnum.GOBLIN)
agent.addDeckCard(TroopEnum.BOWLER)
agent.addDeckCard(TroopEnum.HOGRIDER)
agent.addDeckCard(TroopEnum.MINION)
agent.addDeckCard(TroopEnum.KNIGHT)
agent.addDeckCard(TroopEnum.ROYALEGIANT)
agent.addDeckCard(TroopEnum.ARCHER)
"""

agent.generateDeck()

print(agent.getDeck())

agent.selectTeam(EnumSide['SIDE_1'])
agent.launchGame()

battleField = BattleField.getInstance()


def initArbitrers():
    arbitre = pytactx.Agent(playerId=arbitrerSecret,
                             arena="conflicttower",
                             username="demo",
                             password="demo",
                             server="mqtt.jusdeliens.com",
                             verbosity=2)

    arbitre.ruleArena(
        "bgImg", "https://raw.githubusercontent.com/DAMIENLRY/ConflictTower/main/background.png")
    arbitre.ruleArena("gridColumns", COLUMNS)
    arbitre.ruleArena("gridRows", ROWS)
    arbitre.ruleArena("map", battleField.getMap())
    arbitre.ruleArena("mapFriction", [0,1,1,1,1,1])
    arbitre.ruleArena("mapImgs", [
                       "", "rgba(0,0,0,0)", "https://raw.githubusercontent.com/DAMIENLRY/ConflictTower/main/assets/explosive-balloon.png", "https://raw.githubusercontent.com/DAMIENLRY/ConflictTower/main/assets/bowler.png", "https://raw.githubusercontent.com/DAMIENLRY/ConflictTower/main/assets/gobelin.png", "https://raw.githubusercontent.com/DAMIENLRY/ConflictTower/main/assets/hog-rider.png"])

    return arbitre


def main():
    arbitre = initArbitrers()

    ballon = BallonCard(EnumSide.SIDE_1,2,1)
    bowler = BowlerCard(EnumSide.SIDE_2,17,3)

    battleField.addTroop(ballon)
    battleField.addTroop(bowler)

    while True:
        arbitre.ruleArena("map", battleField.getMap())
        arbitre.update()
        time.sleep(0.1)

main()
