import random
from typing import List, Set
from j2l.pytactx.agent import Agent

from enums.EnumCard import EnumCard
from enums.EnumSide import EnumSide

class AgentTower:
    """
    Class representing an agent for tower defense in the game.

    Attributes:
        _agent: An instance of the Agent class for communication.
        _deck: A set representing the deck of cards for the agent.
        _deckPlayed: A list representing the cards played from the deck.
        _team: EnumSide representing the team of the agent.
    """

    _agent: Agent
    _deck: Set[EnumCard]
    _deckPlayed: List[EnumCard]
    _team: EnumSide
    
    def __init__(self,playerId:str or None=None, arena:str or None=None, username:str or None=None, password:str or None=None, server:str or None=None, port:int=1883, imgOutputPath:str or None="img.jpeg", autoconnect:bool=True, waitArenaConnection:bool=True, verbosity:int=3, robotId:str or None="_", welcomePrint:bool=True, sourcesdir:str or None=None):
        """
        Initializes the AgentTower instance.

        Parameters:
            playerId (str, optional): Player ID for the agent. Defaults to None.
            arena (str, optional): Arena for the agent. Defaults to None.
            username (str, optional): Username for the agent. Defaults to None.
            password (str, optional): Password for the agent. Defaults to None.
            server (str, optional): Server for the agent. Defaults to None.
            port (int, optional): Port for the agent. Defaults to 1883.
            imgOutputPath (str, optional): Image output path for the agent. Defaults to "img.jpeg".
            autoconnect (bool, optional): Whether to autoconnect. Defaults to True.
            waitArenaConnection (bool, optional): Whether to wait for arena connection. Defaults to True.
            verbosity (int, optional): Verbosity level. Defaults to 3.
            robotId (str, optional): Robot ID for the agent. Defaults to "_".
            welcomePrint (bool, optional): Whether to print welcome message. Defaults to True.
            sourcesdir (str, optional): Sources directory for the agent. Defaults to None.
        """
        self._agent = Agent(playerId, arena, username, password, server, port, imgOutputPath, autoconnect, waitArenaConnection, verbosity, robotId, welcomePrint, sourcesdir)
        self._deck = set()
        
    def set_deck(self, deck:List[EnumCard]) -> None:
        """
        Sets the deck of the agent.

        Parameters:
            deck (List[EnumCard]): List of EnumCard representing the deck.
        """
        self._deck = deck
        
    def get_deck(self) -> List[EnumCard]:
        """
        Gets the deck of the agent.

        Returns:
            List[EnumCard]: List of EnumCard representing the deck.
        """
        return self._deck
    
    def add_deck_card(self, troop: EnumCard) -> None:
        """
        Adds a card to the deck.

        Parameters:
            troop (EnumCard): The card to be added.
        """
        if troop in self._deck: return
        self._deck.add(troop)
        
    def remove_deck_card(self, troop: EnumCard) -> None:
        """
        Removes a card from the deck.

        Parameters:
            troop (EnumCard): The card to be removed.
        """
        if not(troop in self._deck): return
        self._deck.remove(troop)
        
    def select_team(self, team: EnumSide):
        """
        Selects the team for the agent.

        Parameters:
            team (EnumSide): The team to be selected.
        """
        self._team = team
        self._agent.team = team.value
        
    def launch_game(self) -> None:
        """
        Launches the game for the agent.
        """
        if len(self._deck) != 8:
            raise Exception(f"Your card deck must contain 8 cards! Use the EnumCard enumeration with the 'addDeckCard' and 'removeDeckCard' methods.")
        if not hasattr(self, '_team'):
            raise Exception(f"Please choose your team! Use the EnumSide enumeration with the 'selectTeam' method.")
        self._agent.connect()
        listDeck = list(self._deck)
        random.shuffle(listDeck)
        self._deckPlayed = list(listDeck)
        self._agent.setColor(0, 0, 0)
        #self._agent.moveTowards(6, 18)
        self._agent.update()
    
    def generate_deck(self) -> None:
        """
        Generates a random deck for the agent.
        """
        deckGenerated = random.sample(list(EnumCard), 8)
        self._deck = set(deckGenerated)
        
    def encode_coords(self, x: int, y: int) -> int:
        """
        Encodes coordinates for placement.

        Parameters:
            x (int): X-coordinate.
            y (int): Y-coordinate.

        Returns:
            int: Encoded coordinates.
        """
        # Limits
        if x < 0 or x > 12 or y < 0 or y > 8:
            raise ValueError("Values of x and y must be between 0 and 12 for x, and between 0 and 8 for y.")
        # Encoding coordinates
        return (x << 4) | y
        
    def place_card(self, slot: int, x: int, y: int) -> None:
        """
        Places a card on the arena.

        Parameters:
            slot (int): Slot number for the card.
            x (int): X-coordinate for placement.
            y (int): Y-coordinate for placement.
        """
        if(not( 1 <= slot <= 4)): raise("You must choose a card located on slot 1, 2, 3, 4.")
        card = (self._deckPlayed.pop(slot)).value()
        #self._agent.setColor(self._team.value, card.getId(), placement.value)
        self._agent.setColor(self._agent.x, 3, self.encode_coords(x, y))
        self._agent.update()
        self._deckPlayed.append(card)
        
    def get_deck(self) -> None:
        """
        Gets the cards in play.

        Returns:
            None: List of cards in play.
        """
        return self._deckPlayed[:4]
    
    def get_copper(self) -> int:
        """
        Gets the amount of copper.

        Returns:
            int: Amount of copper.
        """
        return self._agent.ammo
        
    def update(self) -> None:
        """
        Updates the agent.
        """
        self._agent.update()
    
    def disconect(self) -> None:
        """
        Disconnects the agent.
        """
        self._agent.disconnect()
    
    def print(self):
        """
        Prints information about the agent.
        """
        print("Deck: " + str(self._deck))
