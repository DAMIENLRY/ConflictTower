from dotenv import load_dotenv
import os
import time
import sys
import threading

from res.BattleField import BattleField
from res.game.MapFrictionWrapper import MapFrictionWrapper
from res.game.globaleVariable import COLUMNS, ROWS, TIME, TIME_TO_GET_COPPER, MAX_COPPER
from res.troops.enums.EnumTroop import EnumTroop

# Obtenez le chemin du répertoire parent de ConflictTower (c'est-à-dire le dossier contenant ConflictTower)
current_file = os.path.abspath(__file__)  # Chemin actuel du script en cours
parent_directory = os.path.dirname(os.path.dirname(current_file))  # Chemin du répertoire parent
sys.path.append(parent_directory)  # Ajoute le répertoire parent au chemin de recherche

from api.j2l.pytactx.agent import Agent

load_dotenv()
arbitrerSecret = os.getenv('arbitrerSecret')

battleField = BattleField.getInstance()

def initArbitrers():
    arbitre = Agent(playerId=arbitrerSecret,
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

def getAgentById(arbitre: Agent, id: int):
    for key, value in arbitre.range.items():
        if value['x'] == id:
            return key, value
    return False

def changeColorListener(arbitre: Agent, callback):
    playerColor = getColorOfPlayers(arbitre.range)
    while True:
        newPlayerColor = getColorOfPlayers(arbitre.range)
        for name, color in newPlayerColor.items():
            if playerColor[name] != color:
                print(name, ' changement de couleur : ', color)
                playerColor[name] = color
                callback(arbitre, playerColor[name])

def getColorOfPlayers(agents: dict):
    playerColor = {}
    for key, value in agents.items():
        playerColor[key] = value['led']
    return playerColor

def decode_coords(encoded):
    x = (encoded >> 4) & 0b1111  # Récupération des 4 premiers bits pour x
    y = encoded & 0b1111  # Récupération des 4 derniers bits pour y
    return x, y + 1

def placeCardOnBattlefield(arbitre: Agent, playerColor):
    playerName, player = getAgentById(arbitre, playerColor[0])
    for troop in EnumTroop: 
        spawnTroop = troop.value(player['team'])
        if spawnTroop.getId() == playerColor[1]:
            selectCard = spawnTroop
            if selectCard.getCopperCost() <= player["ammo"]: 
                x, y = decode_coords(playerColor[2])
                if player['team'] == 2:
                    y = ROWS - y - 1
                selectCard.setPosition(y, x)
                arbitre.rulePlayer(playerName, "ammo", player["ammo"] - selectCard.getCopperCost())
            battleField.addTroop(selectCard)
    
def changeLifeListener(arbitre: Agent, callback):
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
    
def add_copper(arbitre: Agent):
    while True:
        for key, value in arbitre.range.items():
            new_copper_amount = value['ammo'] + 10
            if new_copper_amount <= MAX_COPPER: 
                arbitre.rulePlayer(key, "ammo", new_copper_amount)
        time.sleep(TIME_TO_GET_COPPER)

def can_start_game(arbitre: Agent):
    if len(arbitre.range.keys()) < 2: return False
    return True
    
def lunchGame(arbitre: Agent):
    id = 0
    for key, value in arbitre.range.items():
        id += 1
        arbitre.rulePlayer(key, "x", id)
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

def game_is_finised(arbitre: Agent):
    map_rule_manager = MapFrictionWrapper(arbitre)
    if map_rule_manager.getTime() < 0: return True
    return False

def main():
    arbitre = initArbitrers()
    
    while not can_start_game(arbitre):
        print("La game ne peux pas être lancée")
        time.sleep(2)
        
    lunchGame(arbitre)
    print("partie lancée")
    
    while not game_is_finised(arbitre=arbitre) and can_start_game(arbitre):
        arbitre.ruleArena("map", battleField.getMap())
        arbitre.update()
        time.sleep(0.1)

main()