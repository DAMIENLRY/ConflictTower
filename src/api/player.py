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

agent.select_team(EnumSide.DOWN)
agent.launch_game()

print(agent.get_my_tower_life())
print(agent.get_enemy_tower_life())

agent.place_card(2, 3, 2)