from .StateCard import StateCard

class FocusTowerState(StateCard):
    def handle_request(self):
        print("Troop is focusing on the tower.")