from .StateCard import StateCard

class FocusTowerState(StateCard):
    def handle_request(self, card):
        print("Troop is focusing on the tower.")
        card.start_movement_thread()
