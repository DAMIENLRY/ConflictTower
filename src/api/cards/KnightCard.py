from .InterfaceCard import InterfaceCard

class KnightCard(InterfaceCard):
    """
    Represents a Knight card.

    Attributes:
        _ID (int): Identifier for the card.
        _NAME (str): Name of the card.
    """

    _ID = 8
    _NAME = "Chevalier"
    
    def __init__(self) -> None:
        """
        Initializes the KnightCard object.
        """
        super().__init__()
    
    @staticmethod
    def get_card_id() -> int:
        return KnightCard._ID
