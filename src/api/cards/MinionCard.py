from .InterfaceCard import InterfaceCard

class MinionCard(InterfaceCard):
    """
    Represents a Minion card.

    Attributes:
        _ID (int): Identifier for the card.
        _NAME (str): Name of the card.
    """

    _ID = 9
    _NAME = "Gargouilles"
    
    def __init__(self) -> None:
        """
        Initializes the MinionCard object.
        """
        super().__init()
    
    @staticmethod
    def get_card_id() -> int:
        return MinionCard._ID
        
