from abc import ABC, abstractmethod
from typing import List

from cards.enumCard.CardType import CardType
from cards.enumCard.CardSpeed import CardSpeed

class InterfaceCard(ABC):

    ID: int
    NAME: str
    SPEED: CardSpeed
    RANGE: float
    ATTAQUE_SPEED: CardSpeed
    TYPE: CardType
    HEALTH_POINT: int
    POINT: int

    
    
    