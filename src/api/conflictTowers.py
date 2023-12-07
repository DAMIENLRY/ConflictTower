from enum import Enum
import j2l.pytactx.agent as pytactx
from dotenv import load_dotenv
import os
import time
import sys
import threading

from agentTower import AgentTower

# Obtenez le chemin du répertoire parent de ConflictTower (c'est-à-dire le dossier contenant ConflictTower)
current_file = os.path.abspath(__file__)  # Chemin actuel du script en cours
parent_directory = os.path.dirname(os.path.dirname(current_file))  # Chemin du répertoire parent
sys.path.append(parent_directory)  # Ajoute le répertoire parent au chemin de recherche

from server.res.BattleField import BattleField

from server.res.cards.enums.EnumSide import EnumSide
from server.res.cards.enums.EnumPlacement import EnumPlacement
from server.res.cards.BallonCard import BallonCard
from server.res.cards.BowlerCard import BowlerCard
from server.res.cards.GoblinCard import GoblinCard
from server.res.cards.HogRiderCard import HogRiderCard
from server.res.cards.InterfaceCard import InterfaceCard
from api.enums.TroopEnum import TroopEnum
import api.towerFinder as tf
from api.MapFrictionWrapper import MapFrictionWrapper

from globaleVariable import COLUMNS, ROWS

load_dotenv()
arbitrerSecret = os.getenv('arbitrerSecret')

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
    arbitre.ruleArena("info", " 🟠 3 - 7  💗 432 - 667 ⌛ 2:59")

    map_rule_manager = MapFrictionWrapper(arbitre)

    map_rule_manager.add_friction(0, 0, "")
    map_rule_manager.add_friction(1, 1, "rgba(0,0,0,0)")
    map_rule_manager.add_friction(2, 1, "https://raw.githubusercontent.com/DAMIENLRY/ConflictTower/main/assets/explosive-balloon.png")
    map_rule_manager.add_friction(3, 1, "https://raw.githubusercontent.com/DAMIENLRY/ConflictTower/main/assets/bowler.png")
    map_rule_manager.add_friction(4, 1, "https://raw.githubusercontent.com/DAMIENLRY/ConflictTower/main/assets/gobelin.png")
    map_rule_manager.add_friction(5, 1, "https://raw.githubusercontent.com/DAMIENLRY/ConflictTower/main/assets/hog-rider.png")

    #damages
    map_rule_manager.add_friction(13, 0, "https://raw.githubusercontent.com/DAMIENLRY/ConflictTower/main/assets/damages/3.png")
    map_rule_manager.add_friction(15, 0, "https://raw.githubusercontent.com/DAMIENLRY/ConflictTower/main/assets/damages/5.png")
    map_rule_manager.add_friction(18, 0, "https://raw.githubusercontent.com/DAMIENLRY/ConflictTower/main/assets/damages/8.png")
    map_rule_manager.add_friction(110, 0, "https://raw.githubusercontent.com/DAMIENLRY/ConflictTower/main/assets/damages/10.png")
    map_rule_manager.add_friction(115, 0, "https://raw.githubusercontent.com/DAMIENLRY/ConflictTower/main/assets/damages/15.png")
    map_rule_manager.add_friction(120, 0, "https://raw.githubusercontent.com/DAMIENLRY/ConflictTower/main/assets/damages/20.png")
    map_rule_manager.add_friction(125, 0, "https://raw.githubusercontent.com/DAMIENLRY/ConflictTower/main/assets/damages/25.png")

    return arbitre

def changeColorListener(arbitre: pytactx.Agent, callback):
    playerColor = getColorOfPlayers(arbitre.range)
    while True:
        newPlayerColor = getColorOfPlayers(arbitre.range)
        for name, color in newPlayerColor.items():
            if playerColor[name] != color:
                playerColor[name] = color
                callback(playerColor[name])

def getColorOfPlayers(agents: dict):
    playerColor = {}
    for key, value in agents.items():
        playerColor[key] = value['led']
    return playerColor

def placeCardOnBattlefield(player):
    print("Changement de couleur")
    print(player)
    playerTeam = EnumSide.SIDE_1
    if player[0] == 2: playerTeam = EnumSide.SIDE_2
    selectCard: InterfaceCard = BowlerCard(playerTeam)
    for troop in TroopEnum:
        spawnTroop = troop.value(playerTeam)
        if spawnTroop.getId() == player[1]:
            selectCard = spawnTroop
    print(selectCard._x_position, selectCard._y_position)
    selectCard.setPosition(5, 5)
    print(selectCard._x_position, selectCard._y_position)
    battleField.addTroop(selectCard)

def main():
    arbitre = initArbitrers()

    color_listener_thread = threading.Thread(target=changeColorListener, args=(arbitre, placeCardOnBattlefield))
    color_listener_thread.daemon = True
    color_listener_thread.start()

    agent = AgentTower(playerId="667VELIB",
						arena="conflicttower",
						username="demo",
						password="demo",
						server="mqtt.jusdeliens.com",
						verbosity=2)

    agent.generateDeck()

    agent.selectTeam(EnumSide.SIDE_1)
    agent.launchGame()

    agent.getDeck()

    agent.placeCard(2, EnumPlacement["CENTER"])

    agent.getDeck()

    while True:
        arbitre.ruleArena("map", battleField.getMap())
        arbitre.update()
        time.sleep(0.1)

main()
