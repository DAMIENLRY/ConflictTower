from abc import ABC
from .InterfaceCase import InterfaceCase
from .enums.EnumEntitySpeed import EnumEntitySpeed
from .enums.EnumEntityType import EnumEntityType
from .states.StateTroop import StateTroop
from .states.FocusTowerState import FocusTowerState
from .states.DeadState import DeadState
import sys
import os
import threading

current_file = os.path.abspath(__file__)
parent_directory = os.path.dirname(os.path.dirname(current_file))
sys.path.append(parent_directory)

from game.globaleVariable import COLUMNS, ROWS, TOWER_SIDE_1, TOWER_SIDE_2

class InterfaceTroop(InterfaceCase, ABC):

    _SPEED: EnumEntitySpeed
    _RANGE: int
    _ATTAQUE_SPEED: EnumEntitySpeed
    _ATTACK_DAMAGE: int
    _TYPE: EnumEntityType
    _HEALTH_POINT: int
    _COPPER_COST: int
    _state: StateTroop
    _side: int
    _thread_ia_state: bool
    _battlefield = None
    
    def __init__(self, side: int, x: int, y: int):
        from res.BattleField import BattleField
        super().__init__(x, y)
        self._battlefield = BattleField.get_instance()
        self._side = side
        self._state = FocusTowerState()
        self._thread_ia_state = True
        thread_ia = threading.Thread(target=self.handle_request)
        thread_ia.daemon = True
        thread_ia.start()

    def get_state(self):
        return self._state

    def set_state(self, new_state: StateTroop):
        self._state = new_state

    def get_side(self) -> int:
        return self._side
    
    def get_health(self) -> int:
        return self._HEALTH_POINT
    
    def get_attack_damage(self) -> int:
        return self._ATTACK_DAMAGE
    
    def get_battlefield(self):
        return self._battlefield
    
    def get_attack_speed(self) -> int:
        return self._ATTAQUE_SPEED.value
    
    def get_speed(self) -> int:
        return self._SPEED.value
    
    def is_thread_ia_alive(self) -> bool:
        return self._thread_ia_state
    
    def stop_thread(self):
        self._thread_ia_state = False
    
    def handle_request(self) -> None:
        self._state.handle_request(self)

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
        self.clear_AI()
        
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
        self._state = DeadState()
        self.handle_request()
