from abc import ABC
from .InterfaceCase import InterfaceCase
from .DamageCase import DamageCase
from .enums.EnumEntitySpeed import EnumEntitySpeed
from .enums.EnumEntityType import EnumEntityType
from .states.StateCard import StateCard
from .states.FocusTowerState import FocusTowerState
from .states.AttackTowerState import AttackTowerState
from .states.NoAIState import NoAIState
import time
import sys
import os
import threading

# Obtenez le chemin du répertoire parent de ConflictTower (c'est-à-dire le dossier contenant ConflictTower)
current_file = os.path.abspath(__file__)  # Chemin actuel du script en cours
parent_directory = os.path.dirname(os.path.dirname(current_file)) # Chemin du répertoire parent
sys.path.append(parent_directory)  # Ajoute le répertoire parent au chemin de recherche

from game.globaleVariable import COLUMNS, ROWS, TOWER_SIDE_1, TOWER_SIDE_2
from game.towerFinder import path_to_tower

class InterfaceTroop(InterfaceCase, ABC):

    _ID: int
    _NAME: str
    _x_position: int
    _y_position: int
    _x_prev_position: int
    _y_prev_position: int
    _SPEED: EnumEntitySpeed
    _RANGE: int
    _ATTAQUE_SPEED: EnumEntitySpeed
    _ATTACK_DAMAGE: int
    _TYPE: EnumEntityType
    _HEALTH_POINT: int
    _COPPER_COST: int
    _state: StateCard
    _side: int
    _stop_movement = True
    _stop_attack = False
    _stop_attack_tower_thread = False
    _battlefield = None
    
    def __init__(self):
        from res.BattleField import BattleField
        self._battlefield = BattleField.get_instance()

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, new_state: StateCard):
        self._state = new_state

    def get_side(self) -> int:
        return self._side

    def set_position(self, x: int, y: int) -> None:
        self._x_position = x
        self._y_position = y

    def is_within_bounds(self, x, y):
        return 0 <= x < ROWS and 0 <= y < COLUMNS

    def reduce_health(self, damage_amount):
        self._HEALTH_POINT -= damage_amount
        if self._HEALTH_POINT <= 0:
            self.handle_defeat()
            self._HEALTH_POINT = 0

    def handle_defeat(self):
        print(f"{self.__class__.__name__} a été vaincu.")
        self._battlefield.remove_troop(self)


    def start_attack_thread(self):
        self.attack_thread = threading.Thread(target=self.attack_loop)
        self.attack_thread.start()

    def stop_attack_thread(self):
        self._stop_attack = True
        
    def stop_attack_tower_thread(self):
        self._stop_attack_tower_thread = True
        

    def attack_loop(self):
        self._stop_attack = False
        while not self._stop_attack and self._HEALTH_POINT > 0:
            opponent = self.opponent_in_range()
            print('opponent : ', opponent)
            if opponent:
                opponent_empty_case = self.get_nearest_empty_case(opponent._x_position, opponent._y_position, opponent._RANGE)
                if opponent_empty_case is not False:
                    dmgCase = DamageCase(self._ATTACK_DAMAGE, opponent_empty_case[0], opponent_empty_case[1])

                    self._battlefield.add_damage_case(dmgCase)
                    time.sleep(0.3)
                    self._battlefield.remove_damage_case(dmgCase)

                    opponent_card = self._battlefield.is_occupied_by_opponent(self, opponent._x_position, opponent._y_position)
                    opponent_card.reduce_health(self._ATTACK_DAMAGE)
                    if opponent_card._HEALTH_POINT <= 0:
                        self._stop_attack = True

            if not self._stop_attack and self._HEALTH_POINT > 0:
                time.sleep(self.get_attack_speed_interval())

        self.state = FocusTowerState()
        self.state.handle_request(self)

    def start_attack_tower_thread(self):
        self.attack_tower_thread = threading.Thread(target=self.attack_tower_loop)
        self.attack_tower_thread.start()
        
    def attack_tower_loop(self):
        self._stop_attack_tower_thread = False
        while not self._stop_attack_tower_thread:
            self._battlefield.attack_tower(self._side, self._ATTACK_DAMAGE)
            time.sleep(self.get_attack_speed_interval())

    def start_movement_thread(self):
        path = path_to_tower((self.get_x(),self.get_y()),self.get_tower_focus_coordoonates())
        self.movement_thread = threading.Thread(target=self.movement_loop, args=(path,))
        self.movement_thread.start()

    def stop_movement_thread(self):
        self._stop_movement = True

    def movement_loop(self, path):
        self._stop_movement = False
        while len(path) != 0:
            x, y = path.pop(0)
            if self._stop_movement:
                break
            self.opponent_in_range()
            self.set_location(x, y)
            time.sleep(self.get_move_speed_interval())
            print(path)
            if len(path) == 0:
                self.state = AttackTowerState()
                self._state.handle_request(self)
        print("Movement thread stopped.")


    def get_attack_speed_interval(self):
        return self._ATTAQUE_SPEED.value

    def get_move_speed_interval(self):
        return self._SPEED.value

    def get_tower_focus_coordoonates(self):
        return TOWER_SIDE_2[0] if self.get_side() == 1 else TOWER_SIDE_1[0]

    def set_location(self, x: int, y: int):
        if x>=1 and x<=ROWS-1 and y>=0 and y<=COLUMNS-1:
            if self._x_position and self._y_position:
                self._x_prev_position = self._x_position
                self._y_prev_position = self._y_position
            self._x_position = x
            self._y_position = y
            self._battlefield.on_update_map()
        else:
            return False

    def get_nearest_empty_case(self, x_op, y_op, range_op):
        for dx, dy in [
            (-1,0), (1,0), (0,-1), (0,1),
            (-1,-1), (1,1), (-1,1), (1,-1)
        ]:
            target_x, target_y = dx + x_op, dy + y_op

            if self.is_within_bounds(target_x, target_y):
                empty_case = self._battlefield.is_case_empty(target_x, target_y)
                if empty_case:
                    return (target_x,target_y)
        return False

    def get_copper_cost(self) -> int:
        return self._COPPER_COST

    def opponent_in_range(self):
        offsets = [
            (dx, dy) for dx in range(-self._RANGE, self._RANGE + 1)
            for dy in range(-self._RANGE, self._RANGE + 1)
            if not (dx == 0 and dy == 0)
        ]
        for dx, dy in offsets:
            target_x, target_y = dx + self._x_position, dy + self._y_position
            if self.is_within_bounds(target_x, target_y):
                opponent = self._battlefield.is_occupied_by_opponent(self, target_x, target_y)
                if opponent:
                    return opponent
        return False
    
    def clear_AI(self):
        self._state = NoAIState()
        self._state.handle_request(self)
