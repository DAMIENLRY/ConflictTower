import j2l.pytactx.agent as pytactx
from dotenv import load_dotenv
import os
import time

load_dotenv()
arbitrerSecret = os.getenv('arbitrerSecret')

COLUMNS = 13
ROWS = 21
map = [[0 for j in range(COLUMNS)] for i in range(ROWS)]

"""agent = pytactx.Agent(playerId="667VELIB",
						arena="conflicttower",
						username="demo",
						password="demo",
						server="mqtt.jusdeliens.com",
						verbosity=2)"""

def initArbitrers():
	arbitre1 = pytactx.Agent(playerId=arbitrerSecret,
						arena="conflicttower",
						username="demo",
						password="demo",
						server="mqtt.jusdeliens.com",
						verbosity=2)
	arbitre1.moveTowards
	time.sleep(0.5)
	"""	
	for i in range(ROWS):
		for j in range(COLUMNS):
			if (i==0 or i==ROWS-1) or (j==0 or j==COLUMNS-1):
				map[i][j] = 1
	"""

	for i in range(COLUMNS):
		if i not in (2,3,9,10):
			map[10][i] = 1
	

	arbitre1.ruleArena("bgImg", "https://raw.githubusercontent.com/DAMIENLRY/ConflictTower/main/background.png")
	arbitre1.ruleArena("gridColumns", COLUMNS)
	arbitre1.ruleArena("gridRows", ROWS)
	arbitre1.ruleArena("map", map)
	arbitre1.ruleArena("mapFriction", [0,1,1,1])
	#arbitre1.ruleArena("mapImgs", ["","rgba(255,255,255,1)"])
	arbitre1.ruleArena("mapImgs", ["","","https://raw.githubusercontent.com/DAMIENLRY/ConflictTower/main/assets/explosive-balloon.png"])

	return arbitre1

def main():
	arbitre1 = initArbitrers()
	map[8][0] = 0
	map[8][1] = 0

	while True:
		print("")

main()