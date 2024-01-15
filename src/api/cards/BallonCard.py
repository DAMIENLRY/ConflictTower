from .InterfaceCard import InterfaceCard

class BallonCard(InterfaceCard):
    """
    Represents a Ballon card.

    Attributes:
        _ID (int): Identifier for the card.
        _NAME (str): Name of the card.
    """
    
    _ID = 2
    _NAME = "Ballon"

    def __init__(self) -> None:
        """
        Initializes the BallonCard object.
        """
        super().__init__()
    
    @staticmethod
    def get_card_id() -> int:
        """
        Gets the identifier of the Ballon card.

        Returns:
            int: Identifier of the Ballon card.
        """
        return BallonCard._ID
