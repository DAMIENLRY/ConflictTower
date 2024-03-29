import time

from .StateTroop import StateTroop
from res.troops.states.AttackTowerState import AttackTowerState
from res.game.towerFinder import path_to_tower

class FocusTowerState(StateTroop):
    """
    Represents the state where a troop focuses on moving towards the enemy tower.

    Methods:
        handle_request(troop): Handles the troop's state when it is focusing on the tower.

    Attributes:
        None
    """

    def handle_request(self, troop):
        """
        Handles the troop's state when it is focusing on the tower.

        Parameters:
            troop: Troop object representing the troop focusing on the tower.

        Returns:
            None
        """
        path = path_to_tower((troop.get_x(), troop.get_y()), troop.get_tower_focus_coordinates())
        print("Troop is focusing on the tower.")
        while len(path) != 0 and troop.is_thread_ia_alive():
            x, y = path.pop(0)
            troop.opponent_in_range()
            troop.set_location(x, y)
            time.sleep(troop.get_speed())
            if troop.get_health() <= 0:
                from res.troops.states.DeadState import DeadState
                troop.set_state(DeadState())
                troop.handle_request()
            if troop.opponent_in_range():
                from res.troops.states.AttackState import AttackState
                troop.set_state(AttackState())
                troop.handle_request()
        print("Movement thread stopped.")
        troop.set_state(AttackTowerState())
        troop.handle_request()
