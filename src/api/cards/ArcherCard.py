from .InterfaceCard import InterfaceCard

class ArcherCard(InterfaceCard):
    """
    Represents an Archer card.

    Attributes:
        _ID (int): Identifier for the card.
        _NAME (str): Name of the card.
    """
        
    def __init__(self) -> None:
        """
        Initializes the ArcherCard object.
        """
        self._ID = 7
        self._NAME = "Archer"
