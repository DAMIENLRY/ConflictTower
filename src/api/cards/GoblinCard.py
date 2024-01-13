from .InterfaceCard import InterfaceCard

class GoblinCard(InterfaceCard):
    """
    Represents a Goblin card.

    Attributes:
        _ID (int): Identifier for the card.
        _NAME (str): Name of the card.
    """

    def __init__(self) -> None:
        """
        Initializes the GoblinCard object.
        """
        self._ID = 4
        self._NAME = "Gobelin"
