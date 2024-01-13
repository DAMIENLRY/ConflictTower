from .StateCard import StateCard

class AttackTowerState(StateCard):
    def handle_request(self,card):
        print("Troop is attacking tower.")
        card.stop_movement_thread()
        card.start_attack_tower_thread()
