from abc import ABC

class InterfaceCard(ABC):
    """
    Abstract base class for representing a generic card in a game.

    Attributes:
        _ID (int): Unique identifier for the card.
        _NAME (str): Name of the card.
    """
    
    _ID: int
    _NAME: str
