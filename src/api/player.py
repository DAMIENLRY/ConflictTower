from agentTower import AgentTower
from enums.EnumSide import EnumSide
from enums.EnumPlacement import EnumPlacement

agent = AgentTower(playerId="667VELIB",
						arena="conflicttower",
						username="demo",
						password="demo",
						server="mqtt.jusdeliens.com",
						verbosity=2)
    
agent2 = AgentTower(playerId="EKIP",
                    arena="conflicttower",
                    username="demo",
                    password="demo",
                    server="mqtt.jusdeliens.com",
                    verbosity=2)

agent.generateDeck()

agent.selectTeam(EnumSide.SIDE_1)
agent.launchGame()

agent2.generateDeck()

agent2.selectTeam(EnumSide.SIDE_2)
agent2.launchGame()

print(agent.getDeck())

agent.placeCard(2, 12, 5)
agent2.placeCard(2, 12, 5)