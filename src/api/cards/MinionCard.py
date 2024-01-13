from .InterfaceCard import InterfaceCard

class MinionCard(InterfaceCard):
    """
    Represents a Minion card.

    Attributes:
        _ID (int): Identifier for the card.
        _NAME (str): Name of the card.
    """

    def __init__(self) -> None:
        """
        Initializes the MinionCard object.
        """
        self._ID = 9
        self._NAME = "Gargouilles"
