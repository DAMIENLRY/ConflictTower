from .StateCard import StateCard
import api.towerFinder as tf

class FocusTowerState(StateCard):
    def handle_request(self, card):
        print("Troop is focusing on the tower.")
        coords = tf.pathToTower((card.getX(),card.getY()),card.getTowerFocusCoordoonates())
        card.start_movement_thread(coords)
