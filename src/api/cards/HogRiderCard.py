from .InterfaceCard import InterfaceCard

class HogRiderCard(InterfaceCard):
    """
    Represents a Hog Rider card.

    Attributes:
        _ID (int): Identifier for the card.
        _NAME (str): Name of the card.
    """

    def __init__(self) -> None:
        """
        Initializes the HogRiderCard object.
        """
        self._ID = 5
        self._NAME = "Chevaucheur de cochon"
