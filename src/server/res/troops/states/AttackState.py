import time

from .StateTroop import StateTroop
from res.troops.DamageCase import DamageCase
from res.troops.states.DeadState import DeadState
from res.troops.states.FocusTowerState import FocusTowerState

class AttackState(StateTroop):
        
    def handle_request(self, troop):
        print("Troop is attacking.")
        while troop.get_health() > 0 and troop.is_thread_ia_alive():
            opponent = troop.opponent_in_range()
            if opponent:
                opponent_empty_case = troop.get_nearest_empty_case(opponent._x_position, opponent._y_position, opponent._RANGE)
                if opponent_empty_case is not False:
                    dmgCase = DamageCase(troop.get_attack_damage(), opponent_empty_case[0], opponent_empty_case[1])

                    troop.get_battlefield().add_damage_case(dmgCase)
                    time.sleep(0.3)
                    troop.get_battlefield().remove_damage_case(dmgCase)

                    opponent_card = troop.get_battlefield().is_occupied_by_opponent(troop, opponent._x_position, opponent._y_position)
                    opponent_card.reduce_health(troop.get_attack_damage())
                    if opponent_card._HEALTH_POINT <= 0:
                        troop.set_state(FocusTowerState())
                        troop.handle_request()

            if troop.get_health() > 0:
                time.sleep(troop.get_attack_speed())

        troop.set_state(DeadState())
        troop.handle_request()
