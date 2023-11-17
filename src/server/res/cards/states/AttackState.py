from .StateCard import StateCard

class AttackState(StateCard):
    def handle_request(self):
        print("Troop is attacking.")
