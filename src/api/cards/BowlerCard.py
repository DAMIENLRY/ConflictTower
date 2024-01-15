from .InterfaceCard import InterfaceCard

class BowlerCard(InterfaceCard):
    """
    Represents a Bowler card.

    Attributes:
        _ID (int): Identifier for the card.
        _NAME (str): Name of the card.
    """

    _ID = 3
    _NAME = "Bowler"
     
    def __init__(self) -> None:
        """
        Initializes the BowlerCard object.
        """
        super().__init__()
    
    @staticmethod
    def get_card_id() -> int:
        """
        Gets the identifier of the Bowler card.

        Returns:
            int: Identifier of the Bowler card.
        """
        return BowlerCard._ID
