from .StateCard import StateCard

class AttackState(StateCard):
    def handle_request(self,card):
        print("Troop is attacking.")
        card.stop_movement_thread()
