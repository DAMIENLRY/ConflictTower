from abc import ABC, abstractmethod

class StateCard(ABC):
    """
    Abstract base class representing the state of a card in the game.
    """
    
    @abstractmethod
    def handle_request(self) -> None:
        """
        Abstract method to handle requests related to the card's state.
        """
        pass
