from typing import List
from enums.EnumCard import EnumCard

class Deck:
    """
    Represents a deck of cards used in the game.

    Attributes:
        _deck (List[EnumCard]): List of EnumCard objects representing the deck.
    """

    def __init__(self, deck: List[EnumCard]):
        """
        Initializes the Deck instance with a given deck of cards.

        Args:
            deck (List[EnumCard]): The initial deck of cards.
        """
        self._deck = deck

    def get_next_card(self) -> EnumCard:
        """
        Retrieves the next card in the deck without advancing the iterator.

        Returns:
            EnumCard: The next card in the deck.
        """
        return self._deck[4]

    def next_hand(self, slot: int) -> EnumCard:
        """
        Retrieves and pops the next card in the deck, advancing the iterator.

        Returns:
            EnumCard: The next card in the deck.
        """
        card = self._deck.pop(slot-1)
        self._deck.append(card)
        return card

    def get_hand(self) -> List[EnumCard]:
        """
        Retrieves the next 4 cards in the deck after the current iterator position without advancing the iterator.

        Returns:
            List[EnumCard]: The next 4 cards in the deck without advancing the iterator.
        """
        return self._deck[:4]

    def get_hand_slot(self, slot: int) -> EnumCard:
        """
        Retrieves the card at the specified slot in the deck.

        Args:
            slot (int): The slot number (1 to 4) for the card.

        Returns:
            EnumCard: The card at the specified slot.
        """
        if slot < 1 or slot > 4:
            raise Exception("Please select a slot between 1 and 4")
        return self.get_hand()[slot-1]
