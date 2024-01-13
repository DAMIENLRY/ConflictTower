from .InterfaceCard import InterfaceCard

class RoyalGiantCard(InterfaceCard):
    """
    Represents a Royal Giant card.

    Attributes:
        _ID (int): Identifier for the card.
        _NAME (str): Name of the card.
    """

    def __init__(self) -> None:
        """
        Initializes the RoyalGiantCard object.
        """
        self._ID = 6
        self._NAME = "Géant Royal"
