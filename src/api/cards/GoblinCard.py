from .InterfaceCard import InterfaceCard

class GoblinCard(InterfaceCard):
    """
    Represents a Goblin card.

    Attributes:
        _ID (int): Identifier for the card.
        _NAME (str): Name of the card.
    """

    _ID = 4
    _NAME = "Goblin"
        
    def __init__(self) -> None:
        """
        Initializes the GoblinCard object.
        """
        super().__init__()
    
    @staticmethod
    def get_card_id() -> int:
        """
        Gets the identifier of the Goblin card.

        Returns:
            int: Identifier of the Goblin card.
        """
        return GoblinCard._ID
