from .InterfaceCard import InterfaceCard

class BallonCard(InterfaceCard):
    """
    Represents a Ballon card.

    Attributes:
        _ID (int): Identifier for the card.
        _NAME (str): Name of the card.
    """

    def __init__(self) -> None:
        """
        Initializes the BallonCard object.
        """
        self._ID = 2
        self._NAME = "Ballon"
