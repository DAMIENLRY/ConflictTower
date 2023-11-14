import j2l.pytactx.agent as pytactx
from dotenv import load_dotenv
import os
import time

load_dotenv()
arbitrerSecret = os.getenv('arbitrerSecret')

agent = pytactx.Agent(playerId="667VELIB",
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
	
	time.sleep(1)

	arbitre1.ruleArena("bgImg", "https://github.com/DAMIENLRY/ConflictTower/blob/main/background.png")
	arbitre1.ruleArena("mapFriction", [0,1,1,1])
	arbitre1.ruleArena("mapImgs", ["rgba(255,255,255,1)","rgba(255,255,255,1)","",""])
	#arbitre1.ruleArena("mapImgs", ["barbare-bg.png","","",""])

	return arbitre1

def main():
	arbitre1 = initArbitrers()
	agent.moveTowards(15,15)

	while True:	
		arbitre1.update()
		agent.update()

main()