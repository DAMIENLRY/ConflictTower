#PLAYER FILE

from agentTower import AgentTower
from enums.EnumSide import EnumSide
from enums.EnumCard import EnumCard

agent = AgentTower(playerId="Player",
						arena="conflicttower",
						username="demo",
						password="demo",
						server="mqtt.jusdeliens.com",
						verbosity=2)

agent.generate_deck()

#agent.add_deck_card(EnumCard.BOWLER)

agent.select_team(EnumSide.DOWN)
agent.launch_game()

#agent.place_card(2,2,2)
