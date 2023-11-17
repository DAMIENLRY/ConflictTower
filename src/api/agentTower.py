from collections import deque
from queue import Queue
import random
from typing import List, Set
import os
import sys
from j2l.pytactx.agent import Agent

# Obtenez le chemin du répertoire parent de ConflictTower (c'est-à-dire le dossier contenant ConflictTower)
current_file = os.path.abspath(__file__)  # Chemin actuel du script en cours
parent_directory = os.path.dirname(os.path.dirname(current_file))  # Chemin du répertoire parent
sys.path.append(parent_directory)  # Ajoute le répertoire parent au chemin de recherche

from api.enums.TroopEnum import TroopEnum
from server.res.cards.enums.EnumSide import EnumSide

class AgentTower:
    
    _agent: Agent
    _deck: Set[TroopEnum]
    _deckPlayed: Queue[TroopEnum]
    _elixir: int
    _team: EnumSide
    
    def __init__(self,playerId:str or None=None, arena:str or None=None, username:str or None=None, password:str or None=None, server:str or None=None, port:int=1883, imgOutputPath:str or None="img.jpeg", autoconnect:bool=True, waitArenaConnection:bool=True, verbosity:int=3, robotId:str or None="_", welcomePrint:bool=True, sourcesdir:str or None=None):
        self._agent = Agent(playerId, arena, username, password, server, port, imgOutputPath, autoconnect, waitArenaConnection, verbosity, robotId, welcomePrint, sourcesdir)
        self._deck = set()
        self._elixir = 0
        
    def setDeck(self, deck:List[TroopEnum]) -> None:
        self._deck = deck
        
    def getDeck(self) -> List[TroopEnum]:
        return self._deck
    
    def addDeckCard(self, troop: TroopEnum) -> None:
        if troop in self._deck: return
        self._deck.add(troop)
        
    def removeDeckCard(self, troop: TroopEnum) -> None:
        if not(troop in self._deck): return
        self._deck.remove(troop)
        
    def selectTeam(self, team: EnumSide):
        self._team = team
        
    def launchGame(self) -> None:
        if len(self._deck) != 8:
            raise Exception(f"Votre deck de carte doit contenir 8 cartes ! Utiliser l'énumération TroopEnum avec les méthodes 'addDeckCard' et 'removeDeckCard'")
        if not hasattr(self, '_team'):
            raise Exception(f"Veuillez choisir votre équipe ! Utiliser l'énumération EnumSide avec la méthode 'selectTeam'")
        self._agent.connect()
        listDeck = list(self._deck)
        random.shuffle(listDeck)
        self._deckPlayed = deque(listDeck)
    
    def generateDeck(self) -> None:
        deckGenerated = random.sample(list(TroopEnum), 8)
        self._deck = set(deckGenerated)
    
    def print(self):
        print("Deck: " + str(self._deck))
        
    
       