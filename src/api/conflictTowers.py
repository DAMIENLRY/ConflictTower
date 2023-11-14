import j2l.pytactx.agent as pytactx
from dotenv import load_dotenv
import os

load_dotenv()
arbitrerSecret = os.getenv('arbitrerSecret')

agent = pytactx.Agent(playerId="joueur",
						arena="conflicttower",
						username="demo",
						password="demo",
						server="mqtt.jusdeliens.com",
						verbosity=2)

def initArbitrers():
	arbitre1 = pytactx.Agent(playerId=arbitrerSecret,
						arena="conflicttower",
						username="demo",
						password="demo",
						server="mqtt.jusdeliens.com",
						verbosity=2)
	
	arbitre1.ruleArena("mapFriction", [0,1,1,1])
	arbitre1.ruleArena("mapImgs", ["","rgba(255,255,255,1)","",""])


while True:
	initArbitrers()
	
	agent.moveTowards(15,15)
	agent.update()
	agent.lookAt((agent.dir + 1) % 4)