import random
import time

from typing import List, Set, Union
from j2l.pytactx.agent import Agent

from enums.EnumCard import EnumCard
from enums.EnumSide import EnumSide
from Deck import Deck

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
    _deckPlayed: Deck
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
        self._agent.setColor(255, 0, 0)
        self.update()
        
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
    
    def get_hand_slot(self, slot: int) -> EnumCard:
        """
        Retrieves the card in the specified hand slot.

        Args:
            slot (int): The hand slot (1 to 4) to retrieve the card from.

        Returns:
            EnumCard: The card in the specified hand slot.

        Raises:
            Exception: If the provided slot is not between 1 and 4.
        """
        if slot < 1 or slot > 4:
            raise Exception("Please select a slot between 1 and 4")
        return self._deckPlayed.get_hand_slot(slot)

    def card_is_in_hand(self, card: EnumCard) -> bool:
        """
        Checks if a specific card is in the player's hand.

        Args:
            card (EnumCard): The card to check for.

        Returns:
            bool: True if the card is in the hand, False otherwise.
        """
        return card in self._deckPlayed.get_hand()
    
    def get_card_slot(self, card: EnumCard) -> Union[int, bool]:
        """
        Retrieves the slot of a specific card in the player's hand.

        Args:
            card (EnumCard): The card to find in the hand.

        Returns:
            Union[int, bool]: The slot number (1 to 4) if the card is in the hand, False otherwise.
        """
        if self.card_is_in_hand(card):
            for slot in range(1, 5):
                if self._deckPlayed.get_hand_slot(slot) == card:
                    return slot
        return False

    
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
        
    def select_team(self, team: EnumSide) -> None:
        """
        Selects the team for the agent.

        Parameters:
            team (EnumSide): The team to be selected.
        """
        self._team = team
        
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
        self._deckPlayed = Deck(list(listDeck))
        time.sleep(2)
        self._agent.setColor(0, self._team.value, 0)
        self._agent.update()
        time.sleep(2)
    
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
        
    def place_card(self, slot: int, x: int, y: int) -> bool:
        """
        Places a card on the arena.

        Parameters:
            slot (int): Slot number for the card.
            x (int): X-coordinate for placement.
            y (int): Y-coordinate for placement.
            
        Returns:
            bool: True if card placed.
        """
        if(not( 1 <= slot <= 4)): raise("You must choose a card located on slot 1, 2, 3, 4.")
        selected_card = self._deckPlayed.get_hand_slot(slot)
        selected_card_cost = self.get_cost_card(selected_card)
        print(self.get_hand())
        if selected_card_cost <= self.get_copper():
            card = (selected_card).value
            self._agent.setColor(1, card.get_card_id(), self.encode_coords(x, y))
            self._deckPlayed.next_hand(slot)
            self._agent.update()
            return True
        return False
    
    def get_next_card(self) -> EnumCard:
        pass
    
    def get_deck_card_slot(self, card: EnumCard) -> int:
        self._deck
        
    def get_hand(self) -> None:
        """
        Gets the cards in play.

        Returns:
            None: List of cards in play.
        """
        return self._deckPlayed.get_hand()
    
    def get_copper(self) -> int:
        """
        Gets the amount of copper.

        Returns:
            int: Amount of copper.
        """
        self.update()
        return self._agent.ammo
    
    def get_team(self) -> int:
        """
        Gets the team ID of the agent.

        Returns:
            int: Team ID of the agent.
        """
        self.update()
        return self._agent.team
    
    def get_cost_card(self, troop: EnumCard) -> int:
        troop_id = str(troop.value.get_card_id())
        return self.get_troops_stats()[troop_id]["cost"]
    
    def get_my_tower_life(self) -> int:
        """
        Gets the remaining life of the agent's tower.

        Returns:
            int: Remaining life of the agent's tower.
        """
        self.update()
        game_info = self._agent.game['info']
        if self.get_team() == 1:
            return int(game_info.split()[3])
        else:
            return int(game_info.split()[1])

        
    def get_enemy_tower_life(self) -> int:
        """
        Gets the remaining life of the enemy's tower.

        Returns:
            int: Remaining life of the enemy's tower.
        """
        game_info = self._agent.game['info']
        if self.get_team() == 1:
            return int(game_info.split()[1])
        else:
            return int(game_info.split()[3])
    
    def get_troops_stats(self) -> List[dict[str, Union[int, str]]]:
        """
        Gets statistics for all troops in the game.

        Returns:
            List[dict[str, Union[int, str]]]: List of dictionaries containing troop statistics.
        """
        self.update()
        return self._agent.game["weapons"][0]["troops"]
    
    def get_troops_on_map(self) -> List[dict[str, Union[int, str]]]:
        """
        Gets information about troops currently on the map.

        Returns:
            List[dict[str, Union[int, str]]]: List of dictionaries containing information about troops on the map.
        """
        self.update()
        return self._agent.game["weapons"][0]["troops_map"]
    
    def get_enemy_troops(self) -> List[dict[str, Union[int, str]]]:
        """
        Gets information about enemy troops currently on the map.

        Returns:
            List[dict[str, Union[int, str]]]: List of dictionaries containing information about enemy troops.
        """
        troops = self.get_troops_on_map()
        enemy = []
        for troop in troops:
            if troop["team"] != self.get_team():
                enemy.append(troop)
        return enemy
    
    def my_tower_is_attacked() -> bool:
        """
        Checks if the player's tower is being attacked.

        Returns:
            bool: True if the player's tower is being attacked, False otherwise
        """
        pass
    
    def enemie_tower_is_attacked() -> bool:
        """
        Checks if the enemy's tower is being attacked.

        Returns:
            bool: True if the enemy's tower is being attacked, False otherwise
        """
        pass

    
    def get_allied_troops(self) -> List[dict[str, Union[int, str]]]:
        """
        Gets information about allied troops currently on the map.

        Returns:
            List[dict[str, Union[int, str]]]: List of dictionaries containing information about allied troops.
        """
        troops = self.get_troops_on_map()
        allies = []
        for troop in troops:
            if troop["team"] == self.get_team():
                allies.append(troop)
        return allies
    
    def update(self) -> None:
        """
        Updates the agent to fetch the latest game state.
        """
        self._agent.update()
    
    def disconnect(self) -> None:
        """
        Disconnects the agent from the game.
        """
        self._agent.disconnect()
    
    def print_info(self) -> None:
        """
        Prints information about the agent.
        """
        print("Deck: " + str(self._deck))
