from .InterfaceCard import InterfaceCard

class RoyalGiantCard(InterfaceCard):
    """
    Represents a Royal Giant card.

    Attributes:
        _ID (int): Identifier for the card.
        _NAME (str): Name of the card.
    """
    
    _ID = 6
    _NAME = "Géant Royal"

    def __init__(self) -> None:
        """
        Initializes the RoyalGiantCard object.
        """
        super().__init__()
    
    @staticmethod
    def get_card_id() -> int:
        return RoyalGiantCard._ID
        
