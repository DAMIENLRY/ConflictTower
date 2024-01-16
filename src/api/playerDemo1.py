#PLAYER FILE

import random

from agentTower import AgentTower
from enums.EnumSide import EnumSide
from enums.EnumCard import EnumCard

agent = AgentTower(playerId="Player1",
						arena="conflicttower",
						username="demo",
						password="demo",
						server="mqtt.jusdeliens.com",
						verbosity=2)

agent.generate_deck()

agent.select_team(EnumSide.UP)
agent.launch_game()

while agent.get_my_tower_life() > 0:
    agent.place_card(random.randint(1, 4), random.randint(0, 12), random.randint(0, 8))
