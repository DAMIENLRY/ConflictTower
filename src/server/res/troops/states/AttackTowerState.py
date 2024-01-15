import time

from .StateTroop import StateTroop
from res.troops.states.DeadState import DeadState

class AttackTowerState(StateTroop):
    """
    Represents the attack tower state of a troop.

    Methods:
        handle_request(troop): Handles the troop's attack on the tower.

    Attributes:
        _stop_attack_tower_thread (bool): Flag to stop the tower attack thread.
    """

    def handle_request(self, troop):
        """
        Handles the troop's attack on the tower.

        Parameters:
            troop: Troop object representing the attacking troop.

        Returns:
            None
        """
        print("Troop is attacking tower.")
        self._stop_attack_tower_thread = False
        while troop.get_health() > 0 and troop.is_thread_ia_alive():
            troop.get_battlefield().attack_tower(troop.get_side(), troop.get_attack_damage())
            time.sleep(troop.get_attack_speed())
        troop.set_state(DeadState())
        troop.handle_request()
