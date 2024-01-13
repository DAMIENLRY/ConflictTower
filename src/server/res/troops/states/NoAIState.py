from .StateCard import StateCard

class NoAIState(StateCard):
    def handle_request(self,card):
        print("Troop is attacking tower.")
        card.stop_movement_thread()
        card.stop_attack_thread()
        card.stop_attack_tower_thread()
