from abc import ABC, abstractmethod

class StateTroop(ABC):
    """
    Abstract base class representing the state of a troop in the game.
    """
    
    @abstractmethod
    def handle_request(self, troop) -> None:
        """
        Abstract method to handle requests related to the troop's state.
        """
        pass
