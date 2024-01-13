from .InterfaceCard import InterfaceCard

class BowlerCard(InterfaceCard):
    """
    Represents a Bowler card.

    Attributes:
        _ID (int): Identifier for the card.
        _NAME (str): Name of the card.
    """

    def __init__(self) -> None:
        """
        Initializes the BowlerCard object.
        """
        self._ID = 3
        self._NAME = "Bouliste"
