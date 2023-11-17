from queue import Queue
from typing import List, Set
import os
import sys
from j2l.pytactx.agent import Agent

# Obtenez le chemin du répertoire parent de ConflictTower (c'est-à-dire le dossier contenant ConflictTower)
current_file = os.path.abspath(__file__)  # Chemin actuel du script en cours
parent_directory = os.path.dirname(os.path.dirname(current_file))  # Chemin du répertoire parent
sys.path.append(parent_directory)  # Ajoute le répertoire parent au chemin de recherche

from api.enums.TroopEnum import TroopEnum

class AgentTower:
    
    _agent: Agent
    _deck: Set[TroopEnum]
    _deckPlayed: Queue[TroopEnum]
    _elixir: int
    
    def __init__(self,playerId:str or None=None, arena:str or None=None, username:str or None=None, password:str or None=None, server:str or None=None, port:int=1883, imgOutputPath:str or None="img.jpeg", autoconnect:bool=True, waitArenaConnection:bool=True, verbosity:int=3, robotId:str or None="_", welcomePrint:bool=True, sourcesdir:str or None=None, deck:Set[TroopEnum] or None=set()):
        self._agent = Agent(playerId, arena, username, password, server, port, imgOutputPath, waitArenaConnection, verbosity, robotId, welcomePrint, sourcesdir)
        self._deck = deck
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

    
    def print(self):
        super().print()
        print("Deck: " + str(self._deck))
        
    
       