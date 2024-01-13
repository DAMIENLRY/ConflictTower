#PLAYER FILE

from agentTower import AgentTower
from enums.EnumSide import EnumSide

agent = AgentTower(playerId="667VELIB",
						arena="conflicttower",
						username="demo",
						password="demo",
						server="mqtt.jusdeliens.com",
						verbosity=2)

agent.generate_deck()

agent.select_team(EnumSide.SIDE_1)
agent.launch_game()

print(agent.get_deck())

agent.place_card(2, 3, 2)