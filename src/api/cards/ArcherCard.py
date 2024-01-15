from .InterfaceCard import InterfaceCard

class ArcherCard(InterfaceCard):
    """
    Represents an Archer card.

    Attributes:
        _ID (int): Identifier for the card.
        _NAME (str): Name of the card.
    """
    
    _ID = 7
    _NAME = "Archer"
        
    def __init__(self) -> None:
        """
        Initializes the ArcherCard object.
        """
        super().__init__()
    
    @staticmethod
    def get_card_id() -> int:
        """
        Gets the identifier of the Archer card.

        Returns:
            int: Identifier of the Archer card.
        """
        return ArcherCard._ID
