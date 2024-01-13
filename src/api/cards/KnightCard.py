from .InterfaceCard import InterfaceCard

class KnightCard(InterfaceCard):
    """
    Represents a Knight card.

    Attributes:
        _ID (int): Identifier for the card.
        _NAME (str): Name of the card.
    """

    def __init__(self) -> None:
        """
        Initializes the KnightCard object.
        """
        self._ID = 8
        self._NAME = "Chevalier"
