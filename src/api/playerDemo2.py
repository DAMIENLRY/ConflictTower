#PLAYER FILE

import random

from agentTower import AgentTower
from enums.EnumSide import EnumSide
from enums.EnumCard import EnumCard

agent = AgentTower(playerId="Player2",
						arena="conflicttower",
						username="demo",
						password="demo",
						server="mqtt.jusdeliens.com",
						verbosity=2)

agent.select_team(EnumSide.DOWN)

agent.add_deck_card(EnumCard.ARCHER)
agent.add_deck_card(EnumCard.BALLON)
agent.add_deck_card(EnumCard.GOBLIN)
agent.add_deck_card(EnumCard.HOGRIDER)
agent.add_deck_card(EnumCard.KNIGHT)
agent.add_deck_card(EnumCard.MINION)
agent.add_deck_card(EnumCard.BOWLER)
agent.add_deck_card(EnumCard.ROYALEGIANT)

agent.launch_game()

def get_cheapest_card_slot():
    slot_cheapest_card = 1
    for card_slot in range(1, 5):
        card = agent.get_hand_slot(card_slot)
        cost = agent.get_cost_card(card)
        if cost < agent.get_cost_card(agent.get_hand_slot(slot_cheapest_card)):
            slot_cheapest_card = card_slot
    return slot_cheapest_card

while agent.get_my_tower_life() > 0:
    cheapest_card_slot = get_cheapest_card_slot()
    card = agent.get_hand_slot(cheapest_card_slot)
    if agent.get_cost_card(card) <= agent.get_copper():
        agent.place_card(cheapest_card_slot, random.randint(0, 12), random.randint(0, 8))
