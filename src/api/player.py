#PLAYER FILE
import time
from agentTower import AgentTower
from enums.EnumSide import EnumSide

agent = AgentTower(playerId="667VELIB",
						arena="conflicttower",
						username="demo",
						password="demo",
						server="mqtt.jusdeliens.com",
						verbosity=2)

agent.generate_deck()

agent.select_team(EnumSide.DOWN)
agent.launch_game()

print(agent._agent.game)

agent.place_card(2, 3, 2)

agent = AgentTower(playerId="EKIP",
						arena="conflicttower",
						username="demo",
						password="demo",
						server="mqtt.jusdeliens.com",
						verbosity=2)

agent.generate_deck()

agent.select_team(EnumSide.UP)
agent.launch_game()

agent.place_card(2, 3, 2)