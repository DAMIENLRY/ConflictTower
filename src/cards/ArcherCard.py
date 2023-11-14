from typing import List
from cards.InterfaceCard import InterfaceCard

from cards.enumCard.CardType import CardType
from cards.enumCard.CardSpeed import CardSpeed

class ArcherCard(InterfaceCard):

    ID: 1
    NAME: "Archer"
    SPEED: CardSpeed["AVERAGE"]
    RANGE: 5
    ATTAQUE_SPEED: CardSpeed["AVERAGE"]
    TYPE: CardType["GROUND"]
    HEALTH_POINT: 100
    