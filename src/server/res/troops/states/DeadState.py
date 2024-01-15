from .StateTroop import StateTroop

class DeadState(StateTroop):
    """
    Represents the dead state of a troop.

    Methods:
        handle_request(troop): Handles the troop's state when it is dead.

    Attributes:
        None
    """

    def handle_request(self, troop):
        """
        Handles the troop's state when it is dead.

        Parameters:
            troop: Troop object representing the dead troop.

        Returns:
            None
        """
        print("Troop is dead.")
        troop.stop_thread()
