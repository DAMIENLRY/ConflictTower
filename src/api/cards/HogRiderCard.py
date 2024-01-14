from .InterfaceCard import InterfaceCard

class HogRiderCard(InterfaceCard):
    """
    Represents a Hog Rider card.

    Attributes:
        _ID (int): Identifier for the card.
        _NAME (str): Name of the card.
    """
    _ID = 5
    _NAME = "Chevaucheur de cochon"

    def __init__(self) -> None:
        """
        Initializes the HogRiderCard object.
        """
        super().__init__()
    
    @staticmethod
    def get_card_id() -> int:
        return HogRiderCard._ID
        
        
