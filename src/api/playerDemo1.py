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

#agent.add_deck_card(EnumCard.BALLON)

agent.select_team(EnumSide.UP)
agent.launch_game()
