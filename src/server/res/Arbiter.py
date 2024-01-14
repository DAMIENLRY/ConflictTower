from typing import List, Union
import time
import threading

from res.BattleField import BattleField
from res.game.MapFrictionWrapper import MapFrictionWrapper
from res.game.globaleVariable import COLUMNS, ROWS, TIME, TIME_TO_GET_COPPER, MAX_COPPER
from res.troops.enums.EnumTroop import EnumTroop
from res.j2l.pytactx.agent import Agent

class Arbiter():
    """
    The Arbiter class manages the game flow and interactions between the game environment and players.

    Attributes:
        _instance (Arbiter): Singleton instance of Arbiter
        _battlefield (BattleField): Instance of the BattleField class
        _agent (Agent): Instance of the Agent class for communication with players
        _copper_thread_state (threading.Event): Thread state for copper replenishment
        _countdown_thread_state (threading.Event): Thread state for game countdown
        _color_listener_thread_state (threading.Event): Thread state for color change listener
    """
    
    _instance: 'Arbiter' = None
    _battlefield: BattleField
    _agent: Agent
    _copper_thread_state: threading.Event
    _countdown_thread_state: threading.Event
    _color_listener_thread_state: threading.Event

    @classmethod
    def get_instance(cls) -> 'Arbiter':
        """
        Retrieves the singleton instance of Arbiter. If it does not exist, creates one.

        Returns:
            Arbiter: The singleton instance of Arbiter
        """
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    def __init__(self,playerId:str or None=None, arena:str or None=None, username:str or None=None, password:str or None=None, server:str or None=None, port:int=1883, imgOutputPath:str or None="img.jpeg", autoconnect:bool=True, waitArenaConnection:bool=True, verbosity:int=3, robotId:str or None="_", welcomePrint:bool=True, sourcesdir:str or None=None) -> None:
        """
        Initializes the Arbiter instance.

        Args:
            playerId (str or None): Player ID
            arena (str or None): Arena name
            username (str or None): Player's username
            password (str or None): Player's password
            server (str or None): Server address
            port (int): Server port
            imgOutputPath (str or None): Path for image output
            autoconnect (bool): Autoconnect flag
            waitArenaConnection (bool): Wait for arena connection flag
            verbosity (int): Verbosity level
            robotId (str or None): Robot ID
            welcomePrint (bool): Welcome message flag
            sourcesdir (str or None): Directory for sources
        """
        if not self.__class__._instance:
            self._battlefield = BattleField.get_instance()
            self._agent = Agent(playerId, arena, username, password, server, port, imgOutputPath, autoconnect, waitArenaConnection, verbosity, robotId, welcomePrint, sourcesdir)
            self.init_arbitrer()
            self._copper_thread_state = threading.Event()
            self._countdown_thread_state = threading.Event()
            self._color_listener_thread_state = threading.Event()
        else:
            raise Exception("Cette classe est un singleton !")
    
    def init_arbitrer(self) -> None:
        """
        Initializes the Arbiter with initial rules for the game arena and map.
        """
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
        map_rule_manager.add_friction(6, 1, "https://raw.githubusercontent.com/DAMIENLRY/ConflictTower/main/assets/royal-giant.png")
        map_rule_manager.add_friction(7, 1, "https://raw.githubusercontent.com/DAMIENLRY/ConflictTower/main/assets/archer.png")
        map_rule_manager.add_friction(8, 1, "https://raw.githubusercontent.com/DAMIENLRY/ConflictTower/main/assets/knight.png")

        #damages
        map_rule_manager.add_friction(13, 0, "https://raw.githubusercontent.com/DAMIENLRY/ConflictTower/main/assets/damages/3.png")
        map_rule_manager.add_friction(15, 0, "https://raw.githubusercontent.com/DAMIENLRY/ConflictTower/main/assets/damages/5.png")
        map_rule_manager.add_friction(18, 0, "https://raw.githubusercontent.com/DAMIENLRY/ConflictTower/main/assets/damages/8.png")
        map_rule_manager.add_friction(110, 0, "https://raw.githubusercontent.com/DAMIENLRY/ConflictTower/main/assets/damages/10.png")
        map_rule_manager.add_friction(115, 0, "https://raw.githubusercontent.com/DAMIENLRY/ConflictTower/main/assets/damages/15.png")
        map_rule_manager.add_friction(120, 0, "https://raw.githubusercontent.com/DAMIENLRY/ConflictTower/main/assets/damages/20.png")
        map_rule_manager.add_friction(125, 0, "https://raw.githubusercontent.com/DAMIENLRY/ConflictTower/main/assets/damages/25.png")
    
    def update(self) -> None:
        """Updates the Arbiter and communicates updates to players."""
        self._agent.update()
    
    def get_agent_by_id(self, id: int) -> Union[str, dict]:
        """
        Retrieves the agent information based on the provided ID.

        Args:
            id (int): The ID of the agent

        Returns:
            Union[str, dict]: Name and information of the agent if found, False otherwise
        """
        for key, value in self._agent.range.items():
            if value['x'] == id:
                return key, value
        return False
    
    def get_agent_by_name(self, name: str) -> Union[str, dict]:
        """
        Retrieves the agent information based on the provided name.

        Args:
            name (str): The name of the agent

        Returns:
            Union[str, dict]: Name and information of the agent if found, False otherwise
        """
        return self._agent.range[name]
    
    def get_agents_by_team(self, team: int) -> List[Union[str, dict]]:
        """
        Retrieves a list of agents belonging to a specific team.

        Args:
            team (int): The team ID

        Returns:
            List[Union[str, dict]]: List of agents belonging to the specified team
        """
        agents = []
        for key, value in self._agent.range.items():
            if value['team'] == team:
                return agents.append(key)
        return agents
    
    def get_color_of_players(self, agents: dict) -> dict[str, tuple[int, int, int]]:
        """
        Retrieves the color information of players from the given agent dictionary.

        Args:
            agents (dict): Dictionary containing information about agents

        Returns:
            dict[str, tuple[int, int, int]]: Dictionary mapping player names to their respective colors
        """
        players_color = {}
        for key, value in agents.items():
            players_color[key] = value['led']
        return players_color
    
    def minuteur(self) -> None:
        """
        Manages the countdown timer for the game and updates the status bar.
        """
        map_rule_manager = MapFrictionWrapper(self._agent)

        temps_restant = TIME
        while temps_restant >= -1 and not self._countdown_thread_state.is_set():
            map_rule_manager.update_status_bar("countdown", temps_restant)
            time.sleep(1)
            temps_restant -= 1
    
    def change_color_listener(self, callback) -> None:
        """
        Monitors color changes of players and triggers a callback on color change.

        Args:
            callback: The callback function to be triggered on color change
        """
        player_color = self.get_color_of_players(self._agent.range)
        while not self._color_listener_thread_state.is_set():
            new_player_color = self.get_color_of_players(self._agent.range)
            for name, color in new_player_color.items():
                if player_color[name] != color:
                    print(name, ' changement de couleur : ', color)
                    player_color[name] = color
                    callback(name, player_color[name])
    
    def add_copper(self) -> None:
        """Periodically adds copper to players based on a timer."""
        while not self._copper_thread_state.is_set():
            for key, value in self._agent.range.items():
                new_copper_amount = value['ammo'] + 10
                if new_copper_amount <= MAX_COPPER: 
                    self._agent.rulePlayer(key, "ammo", new_copper_amount)
            time.sleep(TIME_TO_GET_COPPER)
    
    def change_color_actions(self, player_name, player_color) -> None:
        player = self.get_agent_by_name(player_name)
        color_action = player_color[0]
        self.switch_case_color_action()[color_action](player_name, player, player_color)
        
    def select_team(self, player_name, player, player_color):
        print('team selectyed : ', player_color[1])
        self._agent.rulePlayer(player_name, "team", player_color[1])
        self.update()
    
    def place_card_on_battlefield(self, player_name, player, player_color):
        for troop in EnumTroop: 
            if troop.value.get_troop_id() == player_color[1]:
                if troop.value.get_troop_cost() <= player["ammo"]: 
                    x, y = self.decode_coords(player_color[2])
                    if player['team'] == 2:
                        y = ROWS - y - 1
                    select_card = troop.value(player['team'], y, x)
                    self._agent.rulePlayer(player_name, "ammo", player["ammo"] - select_card.get_copper_cost())
                    self._battlefield.add_troop(select_card)
    
    def switch_case_color_action(self):
        return {
            0: self.select_team,
            1: self.place_card_on_battlefield,
        }
                
    def decode_coords(self, encoded) -> tuple[int, int]:
        """
        Decodes the encoded position information into x and y coordinates.

        Args:
            encoded: The encoded position information

        Returns:
            tuple: x and y coordinates
        """
        x = (encoded >> 4) & 0b1111  # Récupération des 4 premiers bits pour x
        y = encoded & 0b1111  # Récupération des 4 derniers bits pour y
        return x, y + 1
    
    def can_start_game(self) -> bool:
        """
        Checks if the game can start based on the number of connected players.

        Returns:
            bool: True if the game can start, False otherwise
        """
        if len(self._agent.range.keys()) < 2: return False
        return True
    
    def lunch_game(self) -> None:
        """
        Starts the game and manages various threads for game events.
        """
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
        color_listener_thread = threading.Thread(target=self.change_color_listener, args=(self.change_color_actions,))
        color_listener_thread.daemon = True
        color_listener_thread.start()
        
        self._copper_thread_state.clear()
        copper_thread = threading.Thread(target=self.add_copper, args=())
        copper_thread.daemon = True
        copper_thread.start()
        
        print("Partie lancée")
        while not self.game_is_finised():
            self._agent.ruleArena("map", self._battlefield.get_map())
            map_rule_manager = MapFrictionWrapper(self._agent)
            map_rule_manager.update_status_bar('life', self._battlefield.get_life_tower_1(), 1)
            map_rule_manager.update_status_bar('life', self._battlefield.get_life_tower_2(), 2)
            self.update()
        
    def time_out(self) -> bool:
        """
        Checks if the game has timed out.

        Returns:
            bool: True if the game has timed out, False otherwise
        """
        map_rule_manager = MapFrictionWrapper(self._agent)
        if map_rule_manager.get_time() < 0: return True
        return False
    
    def game_is_finised(self) -> bool:
        """
        Checks if the game has finished based on timeout or tower defeat.

        Returns:
            bool: True if the game has finished, False otherwise
        """
        return self.time_out and self._battlefield.tower_defeated()
    
    def disconnect_all_agent(self) -> None:
        """
        Disconnects all agents from the game.
        """
        for key, value in self._agent.range.items():
            self._agent.rulePlayer(key, "connected", False)
    
    def reset_game(self) -> None:
        """
        Resets the game state and disconnects all agents.
        """
        self._countdown_thread_state.set()
        self._color_listener_thread_state.set()
        self._copper_thread_state.set()
        self._battlefield.reset()
        self.disconnect_all_agent()
        time.sleep(10) 