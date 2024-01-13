from typing import List
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
parent_directory = os.path.dirname(os.path.dirname(os.path.dirname(current_file)))  # Chemin du répertoire parent
sys.path.append(parent_directory)  # Ajoute le répertoire parent au chemin de recherche

from api.j2l.pytactx.agent import Agent

class Arbiter():
    
    _instance: 'Arbiter' = None
    _battlefield: BattleField
    _agent: Agent
    _copper_thread_state: threading.Event
    _countdown_thread_state: threading.Event
    _color_listener_thread_state: threading.Event

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    def __init__(self,playerId:str or None=None, arena:str or None=None, username:str or None=None, password:str or None=None, server:str or None=None, port:int=1883, imgOutputPath:str or None="img.jpeg", autoconnect:bool=True, waitArenaConnection:bool=True, verbosity:int=3, robotId:str or None="_", welcomePrint:bool=True, sourcesdir:str or None=None):
        if not self.__class__._instance:
            self._battlefield = BattleField.get_instance()
            self._agent = Agent(playerId, arena, username, password, server, port, imgOutputPath, autoconnect, waitArenaConnection, verbosity, robotId, welcomePrint, sourcesdir)
            self.init_arbitrer()
            self._copper_thread_state = threading.Event()
            self._countdown_thread_state = threading.Event()
            self._color_listener_thread_state = threading.Event()
        else:
            raise Exception("Cette classe est un singleton !")
    
    def init_arbitrer(self):

        self._agent.ruleArena(
            "bgImg", "https://raw.githubusercontent.com/DAMIENLRY/ConflictTower/main/background.png")
        self._agent.ruleArena("gridColumns", COLUMNS)
        self._agent.ruleArena("gridRows", ROWS)
        self._agent.ruleArena("map", self._battlefield.get_map())

        map_rule_manager = MapFrictionWrapper(self._agent)

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

        return self._agent
    
    def update(self):
        self._agent.update()
    
    def get_agent_by_id(self, id: int):
        for key, value in self._agent.range.items():
            if value['x'] == id:
                return key, value
        return False
    
    def get_agents_by_team(self, team: int):
        agents = []
        for key, value in self._agent.range.items():
            if value['team'] == team:
                return agents.append(key)
        return agents
    
    def get_color_of_players(self, agents: dict) -> dict[str, tuple[int, int, int]]:
        players_color = {}
        for key, value in agents.items():
            players_color[key] = value['led']
        return players_color
    
    def minuteur(self):
        map_rule_manager = MapFrictionWrapper(self._agent)

        temps_restant = TIME
        while temps_restant >= -1 and not self._countdown_thread_state.is_set():
            map_rule_manager.update_status_bar("countdown", temps_restant)
            time.sleep(1)
            temps_restant -= 1
        print("Temps écoulé !")
    
    def change_color_listener(self, callback):
        player_color = self.get_color_of_players(self._agent.range)
        while not self._color_listener_thread_state.is_set():
            new_player_color = self.get_color_of_players(self._agent.range)
            for name, color in new_player_color.items():
                if player_color[name] != color:
                    print(name, ' changement de couleur : ', color)
                    player_color[name] = color
                    callback(player_color[name])
    
    def add_copper(self):
        while not self._copper_thread_state.is_set():
            for key, value in self._agent.range.items():
                new_copper_amount = value['ammo'] + 10
                if new_copper_amount <= MAX_COPPER: 
                    self._agent.rulePlayer(key, "ammo", new_copper_amount)
            time.sleep(TIME_TO_GET_COPPER)
    
    def place_card_on_battlefield(self, player_color):
        player_name, player = self.get_agent_by_id(player_color[0])
        for troop in EnumTroop: 
            spawn_troop = troop.value(player['team'])
            if spawn_troop.get_id() == player_color[1]:
                select_card = spawn_troop
                if select_card.get_copper_cost() <= player["ammo"]: 
                    x, y = self.decode_coords(player_color[2])
                    if player['team'] == 2:
                        y = ROWS - y - 1
                    select_card.set_position(y, x)
                    self._agent.rulePlayer(player_name, "ammo", player["ammo"] - select_card.get_copper_cost())
                self._battlefield.add_troop(select_card)
    
    def decode_coords(self, encoded):
        x = (encoded >> 4) & 0b1111  # Récupération des 4 premiers bits pour x
        y = encoded & 0b1111  # Récupération des 4 derniers bits pour y
        return x, y + 1
    
    def can_start_game(self):
        if len(self._agent.range.keys()) < 2: return False
        return True
    
    def lunch_game(self):
        self.init_arbitrer()
        id = 0
        for key, value in self._agent.range.items():
            id += 1
            self._agent.rulePlayer(key, "x", id)
            self._agent.rulePlayer(key, "team", value['led'][0])
            self._agent.rulePlayer(key, "ammo", 60)
            
        self._countdown_thread_state.clear()
        countdown_thread = threading.Thread(target=self.minuteur, args=())
        countdown_thread.daemon = True
        countdown_thread.start()

        self._color_listener_thread_state.clear()
        color_listener_thread = threading.Thread(target=self.change_color_listener, args=(self.place_card_on_battlefield,))
        color_listener_thread.daemon = True
        color_listener_thread.start()
        
        self._copper_thread_state.clear()
        copper_thread = threading.Thread(target=self.add_copper, args=())
        copper_thread.daemon = True
        copper_thread.start()
        
        while not self.game_is_finised():
            self._agent.ruleArena("map", self._battlefield.get_map())
            map_rule_manager = MapFrictionWrapper(self._agent)
            map_rule_manager.update_status_bar('life', self._battlefield.get_life_tower_1(), 1)
            map_rule_manager.update_status_bar('life', self._battlefield.get_life_tower_2(), 2)
            self.update()
        
    def can_start_game(self):
        if len(self._agent.range.keys()) < 2: return False
        return True
    
    def time_out(self):
        map_rule_manager = MapFrictionWrapper(self._agent)
        if map_rule_manager.get_time() < 0: return True
        return False
    
    def game_is_finised(self):
        return self.time_out and self._battlefield.tower_defeated()
    
    def disconnect_all_agent(self):
        for key, value in self._agent.range.items():
            self._agent.rulePlayer(key, "connected", False)
    
    def reset_game(self):
        self._countdown_thread_state.set()
        self._color_listener_thread_state.set()
        self._copper_thread_state.set()
        self._battlefield.reset()
        self.disconnect_all_agent()
        time.sleep(10) 