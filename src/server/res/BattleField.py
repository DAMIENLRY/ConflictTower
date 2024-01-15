from typing import List

from res.game.globaleVariable import COLUMNS, ROWS
from res.troops.InterfaceCase import InterfaceCase
from res.troops.InterfaceTroop import InterfaceTroop
from res.troops.EmptyCase import EmptyCase
from res.troops.ObstacleCase import ObstacleCase
from res.troops.states.FocusTowerState import FocusTowerState
from res.troops.states.AttackState import AttackState
from res.troops.DamageCase import DamageCase

class BattleField:
    """
    This class manages the battlefield. This is a singleton

    Attributes:
        _instance (BattleField): Instance of battlefield (singleton pattern)
        _map (List[List[InterfaceCase]]): Stores the map as a 2D list of InterfaceCase objects
        _troops (List[InterfaceTroop]): List of troops present on the battlefield
        _tower_team_1 (int): Team tower life 1
        _tower_team_2 (int): Team tower life 2
    """

    _instance: 'BattleField' = None
    _map: List[List[InterfaceCase]]
    _troops: List[InterfaceTroop]
    _tower_team_1: int
    _tower_team_2: int

    @classmethod
    def get_instance(cls) -> 'BattleField':
        """
        Returns the singleton instance of BattleField. If it does not exist, creates one.

        Returns:
            BattleField: The singleton instance of BattleField
        """
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    def __init__(self) -> None:
        """
        Initializes the BattleField instance. Ensures that only one instance is created.

        Raises:
            Exception: If an attempt is made to create more than one instance
        """
        if not self.__class__._instance:
            self.init_map()
            self._troops = []
            self._tower_team_1 = 200
            self._tower_team_2 = 200
        else:
            raise Exception("This class is a singleton!")

    def get_map(self) -> List[List[int]]:
        """
        Returns the current state of the map.

        Returns:
            List[List[int]]: A 2D list representing the map, with IDs of InterfaceCase objects
        """
        map: List[List[int]] = []
        for row in range(ROWS):
            line = []
            for column in range(COLUMNS):
                line.append(self._map[row][column].get_id())
            map.append(line)
        return map
    
    def get_troop_dict(self, troop: InterfaceTroop) -> dict:
        return {
            'id': troop.get_id(),
            'name': troop.get_name(),
            'health': troop.get_health(),
            'attack_damage': troop.get_attack_damage(),
            'attack_speed': troop.get_attack_speed(),
            'team': troop.get_side(),
            'speed': troop.get_speed(),
            'x': troop.get_x(),
            'y': troop.get_y(),
            'range': troop.get_range(),
            'type': troop.get_type(),
            'cost': troop.get_copper_cost()
        }
    
    def get_troops_dict(self) -> List[dict]:
        """
        Retrieves a list of dictionaries containing information about all troops on the battlefield.

        Returns:
            List[dict]: List of dictionaries, each containing troop information
        """
        troops = []
        for troop in self._troops:
            troops.append(self.get_troop_dict(troop))
        return troops
            

    def update_map(self) -> None:
        """
        Updates the map based on the current state of troops on the battlefield.
        """
        for troop in self._troops:
            prev_x = troop.get_previous_x()
            prev_y = troop.get_previous_y()
            if prev_x is not None and prev_y is not None:
                if not isinstance(self._map[prev_x][prev_y], DamageCase):
                    self._map[prev_x][prev_y] = EmptyCase(prev_x, prev_y)

            x = troop.get_x()
            y = troop.get_y()
            self._map[x][y] = troop
            
    def on_update_map(self) -> None:
        """
        Wrapper function for updating the map. Called when a troop is added or removed.
        """
        self.update_map()

    def add_troop(self, troop: InterfaceTroop) -> None:
        """
        Adds a troop to the battlefield and updates the map.

        Args:
            troop (InterfaceTroop): The troop to be added
        """
        self._troops.append(troop)
        self.on_update_map()

    def remove_troop(self, troop: InterfaceTroop) -> None:
        """
        Removes a troop from the battlefield and updates the map.

        Args:
            troop (InterfaceTroop): The troop to be removed
        """
        self._troops.remove(troop)
        self._map[troop._x_position][troop._y_position] = EmptyCase()
        self.on_update_map()

    def add_damage_case(self, damage_case):
        """
        Adds a damage case to the battlefield map at the specified position and updates the map.

        Args:
            damage_case (DamageCase): The damage case to be added
        """
        x, y = damage_case.get_x(), damage_case.get_y()
        self._map[x][y] = damage_case
        self.on_update_map()

    def remove_damage_case(self, damage_case):
        """
        Removes a damage case from the battlefield map at the specified position and updates the map.

        Args:
            damage_case (DamageCase): The damage case to be removed
        """
        x, y = damage_case.get_x(), damage_case.get_y()
        self._map[x][y] = EmptyCase(x, y)
        self.on_update_map()

    def init_map(self):
        """
        Initializes the battlefield map, setting up empty cases and placing obstacle cases at specific positions.

        The map is a 2D grid of InterfaceCase objects representing the battlefield.

        - Empty cases are initially placed in each grid cell.
        - Obstacle cases are placed at specific positions defined by the ROWS constant.

        Note: This function is called during the BattleField initialization.
        """
        map: List[List[InterfaceCase]] = []
        for row in range(ROWS):
            line = []
            for column in range(COLUMNS):
                line.append(EmptyCase(row, column))
            map.append(line)
        
        for case in range(ROWS):
            if case in (0, 1, 4, 5, 6, 7, 8, 11, 12):
                map[10][case] = ObstacleCase(row, column)
        
        self._map = map

    
    def reset(self) -> None:
        """
        Resets the battlefield to its initial state.
        """
        self.init_map()
        self._troops = []
        self._tower_team_1 = 200
        self._tower_team_2 = 200

    def is_occupied_by_opponent(self,entity,x,y):
        """
        Checks if a specific position on the battlefield is occupied by an opponent troop.

        Args:
            entity (InterfaceTroop): The troop making the inquiry
            x (int): The x-coordinate on the battlefield
            y (int): The y-coordinate on the battlefield

        Returns:
            Union[InterfaceCase, bool]: The troop occupying the position if it belongs to the opponent, otherwise False
        """
        troop_on_map: InterfaceCase | InterfaceTroop = self._map[x][y]
        if isinstance(troop_on_map, InterfaceTroop):
            if(entity._side != self._map[x][y]._side):
                return troop_on_map
        else:
            return False

    def is_case_empty(self,x,y) -> bool:
        """
        Checks if a specific position on the battlefield is empty.

        Args:
            x (int): The x-coordinate on the battlefield
            y (int): The y-coordinate on the battlefield

        Returns:
            bool: True if the position is empty, False otherwise
        """
        return isinstance(self._map[x][y], EmptyCase)

    def check_and_update_card_states(self) -> None:
        """
        Checks and updates the states of troops on the battlefield based on their proximity to opponents or towers.
        """
        for troop in self._troops:
            opponent = troop.opponent_in_range()
            if opponent and not isinstance(troop.state, AttackState):
                troop.state = AttackState()
                troop.state.handle_request(troop)
            elif not opponent and not isinstance(troop.get_state(), FocusTowerState) and not isinstance(troop.get_state(), AttackState):
                troop.state = FocusTowerState()
                troop.state.handle_request(troop)
    
    def get_life_tower_1(self) -> int:
        """
        Retrieves the remaining life of tower 1.

        Returns:
            int: The remaining life of tower 1
        """
        return self._tower_team_1
    
    def get_life_tower_2(self) -> int:
        """
        Retrieves the remaining life of tower 2.

        Returns:
            int: The remaining life of tower 2
        """
        return self._tower_team_2
    
    def get_case(self, x, y) -> InterfaceCase:
        """
        Retrieves the InterfaceCase object at the specified position on the battlefield.

        Args:
            x (int): The x-coordinate on the battlefield
            y (int): The y-coordinate on the battlefield

        Returns:
            InterfaceCase: The InterfaceCase object at the specified position
        """
        return self._map[x][y]
    
    def tower_defeated(self) -> bool:
        """
        Checks if either tower 1 or tower 2 has been defeated.

        Returns:
            bool: True if either tower has been defeated, False otherwise
        """
        if self._tower_team_1 <= 0 or self._tower_team_2 <= 0:
            return True
        return False

                
    def attack_tower(self, team, damage) -> None:
        """
        Attacks a tower on the battlefield.

        Args:
            team (int): The team of the tower (1 or 2)
            damage (int): The amount of damage to be dealt
        """
        if team == 1:
            self._tower_team_2 -= damage
        else:
            self._tower_team_1 -= damage 
            
    def clear_all_ia(self) -> None:
        """
        Clears the AI state for all troops on the battlefield.
        """
        for troop in self._troops:
            troop.clear_AI()