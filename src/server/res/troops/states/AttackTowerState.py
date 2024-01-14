import time

from .StateTroop import StateTroop
from res.troops.states.DeadState import DeadState


class AttackTowerState(StateTroop):
    
    def handle_request(self, troop):
        print("Troop is attacking tower.")
        self._stop_attack_tower_thread = False
        while troop.get_health() > 0 and troop.is_thread_ia_alive():
            troop.get_battlefield().attack_tower(troop.get_side(), troop.get_attack_damage())
            time.sleep(troop.get_attack_speed())
        troop.set_state(DeadState())
        troop.handle_request()
