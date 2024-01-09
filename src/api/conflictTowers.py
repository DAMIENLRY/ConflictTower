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

from globaleVariable import COLUMNS, ROWS, TIME, TIME_TO_GET_COPPER, MAX_COPPER

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

    map_rule_manager = MapFrictionWrapper(arbitre)

    map_rule_manager.init_status_bar()

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
                print(name, ' changement de couleur : ', color)
                playerColor[name] = color
                callback(playerColor[name])

def getColorOfPlayers(agents: dict):
    playerColor = {}
    for key, value in agents.items():
        playerColor[key] = value['led']
    return playerColor

def placeCardOnBattlefield(player):
    playerTeam = EnumSide.SIDE_1
    if player[0] == 2: playerTeam = EnumSide.SIDE_2
    selectCard: InterfaceCard = BowlerCard(playerTeam)
    for troop in TroopEnum:
        spawnTroop = troop.value(playerTeam)
        if spawnTroop.getId() == player[1]:
            selectCard = spawnTroop
    print('player: ', player)
    if selectCard.getCopperCost() <= player["ammo"]:   
        selectCard.setPosition(5, 5)
        player["ammo"] -= selectCard.getCopperCost()
        battleField.addTroop(selectCard)
    
def changeLifeListener(arbitre: pytactx.Agent, callback):
    playerLife = getLifeOfPlayers(arbitre.range)
    while True:
        newPlayerColor = getLifeOfPlayers(arbitre.range)
        for name, color in newPlayerColor.items():
            if playerLife[name] != color:
                playerLife[name] = color
                callback(arbitre, playerLife[name])
                
def getLifeOfPlayers(agents: dict):
    playerLife = {}
    for key, value in agents.items():
        playerLife[key] = value['life']
    return playerLife

def changeLifeTower(arbitre, player):
    map_rule_manager = MapFrictionWrapper(arbitre)
    map_rule_manager.update_status_bar("life", [])

def minuteur(arbitre):
    map_rule_manager = MapFrictionWrapper(arbitre)

    temps_restant = TIME
    while temps_restant >= -1:
        map_rule_manager.update_status_bar("countdown", temps_restant)
        time.sleep(1)
        temps_restant -= 1
    print("Temps écoulé !")
    
def add_copper(arbitre: pytactx.Agent):
    while True:
        for key, value in arbitre.range.items():
            new_copper_amount = value['ammo'] + 10
            if new_copper_amount <= MAX_COPPER: 
                arbitre.rulePlayer(key, "ammo", new_copper_amount)
        time.sleep(TIME_TO_GET_COPPER)

def can_start_game(arbitre: pytactx.Agent):
    if len(arbitre.range.keys()) < 2: return False
    return True
    
def lunchGame(arbitre: pytactx.Agent):
    robotId = 0
    for key, value in arbitre.range.items():
        robotId += 1
        arbitre.rulePlayer("EKIP", "profile", 0)
        arbitre.rulePlayer(key, "robotId", str(robotId))
        arbitre.rulePlayer(key, "team", value['led'][0])
        arbitre.rulePlayer(key, "ammo", 60)
        
    countdown_thread = threading.Thread(target=minuteur, args=(arbitre,))
    countdown_thread.daemon = True
    countdown_thread.start()

    color_listener_thread = threading.Thread(target=changeColorListener, args=(arbitre, placeCardOnBattlefield))
    color_listener_thread.daemon = True
    color_listener_thread.start()
    
    copper_thread = threading.Thread(target=add_copper, args=(arbitre,))
    copper_thread.daemon = True
    copper_thread.start()

def game_is_finised(arbitre: pytactx.Agent):
    map_rule_manager = MapFrictionWrapper(arbitre)
    if map_rule_manager.getTime() < 0: return True
    return False

def main():
    arbitre = initArbitrers()

    agent = AgentTower(playerId="667VELIB",
						arena="conflicttower",
						username="demo",
						password="demo",
						server="mqtt.jusdeliens.com",
						verbosity=2)
    
    agent2 = AgentTower(playerId="EKIP",
						arena="conflicttower",
						username="demo",
						password="demo",
						server="mqtt.jusdeliens.com",
						verbosity=2)
    
    agent2.generateDeck()

    agent2.selectTeam(EnumSide.SIDE_2)
    agent2.launchGame()
    
    agent.generateDeck()

    agent.selectTeam(EnumSide.SIDE_1)
    agent.launchGame()

    agent.getDeck()
    agent.getDeck()
    
    while not can_start_game(arbitre):
        print("La game ne peux pas être lancée")
        time.sleep(2)
        
    lunchGame(arbitre)
    print("partie lancée")
    
    agent.placeCard(2, EnumPlacement["CENTER"])
    
    while not game_is_finised(arbitre=arbitre) and can_start_game(arbitre):
        arbitre.ruleArena("map", battleField.getMap())
        arbitre.update()
        time.sleep(0.1)

main()