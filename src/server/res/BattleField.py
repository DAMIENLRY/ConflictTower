from typing import List

from res.game.globaleVariable import COLUMNS, ROWS
from res.troops.InterfaceCase import InterfaceCase
from res.troops.InterfaceTroop import InterfaceTroop
from res.troops.EmptyCase import EmptyCase
from res.troops.ObstacleCase import ObstacleCase
from res.troops.ObstacleCase import ObstacleCase
from res.troops.states.FocusTowerState import FocusTowerState
from res.troops.states.AttackState import AttackState
from res.troops.DamageCase import DamageCase


class BattleField:

    _instance: 'BattleField' = None
    _map: List[List[InterfaceCase]]
    _troops: List[InterfaceTroop]
    _tower_team_1: int
    _tower_team_2: int

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    def __init__(self):
        if not self.__class__._instance:
            self.init_map()
            self._troops = []
            self._tower_team_1 = 200
            self._tower_team_2 = 200
        else:
            raise Exception("Cette classe est un singleton !")


    def get_map(self):
        map: List[List[int]] = []
        for row in range(ROWS):
            line = []
            for column in range(COLUMNS):
                line.append(self._map[row][column].get_id())
            map.append(line)
        return map

    def update_map(self):
        for troop in self._troops:
            prev_x = troop.get_previous_x()
            prev_y = troop.get_previous_y()
            if prev_x is not None and prev_y is not None:
                if not isinstance(self._map[prev_x][prev_y], DamageCase):
                    self._map[prev_x][prev_y] = EmptyCase(prev_x, prev_y)

            x = troop.get_x()
            y = troop.get_y()
            self._map[x][y] = troop
        self.check_and_update_card_states()

    def on_update_map(self):
        self.update_map()

    def add_troop(self, troop: InterfaceTroop):
        self._troops.append(troop)
        self.on_update_map()
        troop.state.handle_request(troop)

    def remove_troop(self, troop: InterfaceTroop):
        self._troops.remove(troop)
        self._map[troop._x_position][troop._y_position] = EmptyCase()
        self.on_update_map()

    def add_damage_case(self, damage_case):
        x, y = damage_case.get_x(), damage_case.get_y()
        self._map[x][y] = damage_case
        self.on_update_map()

    def remove_damage_case(self, damage_case):
        x, y = damage_case.get_x(), damage_case.get_y()
        self._map[x][y] = EmptyCase(x, y)
        self.on_update_map()

    def init_map(self):
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
    
    def reset(self):
        self.init_map()
        self._troops = []
        self._tower_team_1 = 200
        self._tower_team_2 = 200

    def is_occupied_by_opponent(self,entity,x,y):
        troop_on_map: InterfaceCase | InterfaceTroop = self._map[x][y]
        #print(troop_on_map,'--------->', InterfaceTroop.__class__)
        # print(self._map[x][y].__class__.__name__, ' ----> ',type(self._map[x][y]))
        # print("Type of self._map[x][y]:", type(self._map[x][y]))
        # print("Is self._map[x][y] an instance of InterfaceTroop?", isinstance(self._map[x][y], InterfaceTroop))
        # print("BowlerTroop bases:", BowlerTroop.__bases__)
        # print("InterfaceTroop bases:", InterfaceTroop.__bases__)
        if isinstance(troop_on_map, InterfaceTroop):
            if(entity._side != self._map[x][y]._side):
                return troop_on_map
        else:
            return False

    def is_case_empty(self,x,y):
        return isinstance(self._map[x][y], EmptyCase)

    def check_and_update_card_states(self):
        for card in self._troops:
            opponent = card.opponent_in_range()
            if opponent and not isinstance(card.state, AttackState):
                card.state = AttackState()
                card.state.handle_request(card)
            elif not opponent and not isinstance(card.state, FocusTowerState) and not isinstance(card.state, AttackState):
                card.state = FocusTowerState()
                card.state.handle_request(card)
    
    def get_life_tower_1(self):
        return self._tower_team_1
    
    def get_life_tower_2(self):
        return self._tower_team_2
    
    def get_case(self, x, y):
        return self._map[x][y]
    
    def tower_defeated(self):
        if self._tower_team_1 <= 0 or self._tower_team_2 <= 0: return True
        return False
                
    def attack_tower(self, team, damage):
        if team == 1:
            self._tower_team_2 -= damage
            print("La tour 2 se fait attaqué ! Il lui reste ", self._tower_team_2, "HP")
        else:
            self._tower_team_1 -= damage 
            print("La tour 1 se fait attaqué ! Il lui reste ", self._tower_team_1, "HP")
            
    def clear_all_ia(self):
        for troop in self._troops:
            troop.clear_AI()