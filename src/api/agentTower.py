import random
from typing import List, Set
from j2l.pytactx.agent import Agent

from enums.EnumCard import EnumCard
from enums.EnumSide import EnumSide

class AgentTower:
    
    _agent: Agent
    _deck: Set[EnumCard]
    _deckPlayed: List[EnumCard]
    _team: EnumSide
    
    def __init__(self,playerId:str or None=None, arena:str or None=None, username:str or None=None, password:str or None=None, server:str or None=None, port:int=1883, imgOutputPath:str or None="img.jpeg", autoconnect:bool=True, waitArenaConnection:bool=True, verbosity:int=3, robotId:str or None="_", welcomePrint:bool=True, sourcesdir:str or None=None):
        self._agent = Agent(playerId, arena, username, password, server, port, imgOutputPath, autoconnect, waitArenaConnection, verbosity, robotId, welcomePrint, sourcesdir)
        self._deck = set()
        
    def set_deck(self, deck:List[EnumCard]) -> None:
        self._deck = deck
        
    def get_deck(self) -> List[EnumCard]:
        return self._deck
    
    def add_deck_card(self, troop: EnumCard) -> None:
        if troop in self._deck: return
        self._deck.add(troop)
        
    def remove_deck_card(self, troop: EnumCard) -> None:
        if not(troop in self._deck): return
        self._deck.remove(troop)
        
    def select_team(self, team: EnumSide):
        self._team = team
        self._agent.team = team.value
        
    def launch_game(self) -> None:
        if len(self._deck) != 8:
            raise Exception(f"Votre deck de carte doit contenir 8 cartes ! Utiliser l'énumération EnumCard avec les méthodes 'addDeckCard' et 'removeDeckCard'")
        if not hasattr(self, '_team'):
            raise Exception(f"Veuillez choisir votre équipe ! Utiliser l'énumération EnumSide avec la méthode 'selectTeam'")
        self._agent.connect()
        listDeck = list(self._deck)
        random.shuffle(listDeck)
        self._deckPlayed = list(listDeck)
        self._agent.setColor(self._team.value, 0, 0)
        #self._agent.moveTowards(6, 18)
        self._agent.update()
    
    def generate_deck(self) -> None:
        deckGenerated = random.sample(list(EnumCard), 8)
        self._deck = set(deckGenerated)
        
    def encode_coords(self, x: int, y: int) -> int:
        # Vérification des limites
        if x < 0 or x > 12 or y < 0 or y > 8:
            raise ValueError("Les valeurs de x et y doivent être comprises entre 0 et 12 pour x et entre 0 et 8 pour y.")
        # Encodage des coordonnées
        return (x << 4) | y
        
    def place_card(self, slot: int, x: int, y: int) -> None:
        if(not( 1 <= slot <= 4)): raise("Vous devez choisir votre carte situé sur le slot 1, 2, 3, 4")
        card = (self._deckPlayed.pop(slot)).value()
        #self._agent.setColor(self._team.value, card.getId(), placement.value)
        self._agent.setColor(self._agent.x, 3, self.encode_coords(x, y))
        self._agent.update()
        self._deckPlayed.append(card)
        
    def get_deck(self) -> None:
        return self._deckPlayed[:4]
    
    def get_copper(self) -> int:
        return self._agent.ammo
        
    def update(self) -> None:
        self._agent.update()
    
    def disconect(self) -> None:
        self._agent.disconnect()
    
    def print(self):
        print("Deck: " + str(self._deck))
        
    
       