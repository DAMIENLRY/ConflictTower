from .StateTroop import StateTroop

class DeadState(StateTroop):
    
    def handle_request(self, troop):
        print("Troop is dead.")
        troop.stop_thread()
