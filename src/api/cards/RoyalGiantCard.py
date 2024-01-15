from .InterfaceCard import InterfaceCard

class RoyalGiantCard(InterfaceCard):
    """
    Represents a Royal Giant card.

    Attributes:
        _ID (int): Identifier for the card.
        _NAME (str): Name of the card.
    """
    
    _ID = 6
    _NAME = "Royal Giant"

    def __init__(self) -> None:
        """
        Initializes the RoyalGiantCard object.
        """
        super().__init__()
    
    @staticmethod
    def get_card_id() -> int:
        """
        Gets the identifier of the Royal Giant card.

        Returns:
            int: Identifier of the Royal Giant card.
        """
        return RoyalGiantCard._ID
