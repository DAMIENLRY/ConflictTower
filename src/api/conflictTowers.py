import j2l.pytactx.agent as pytactx
from dotenv import load_dotenv
import os

load_dotenv()

agent = pytactx.Agent(playerId="31012003",
						arena="conflicttower",
						username="demo",
						password="demo",
						server="mqtt.jusdeliens.com",
						verbosity=2)

arbitrerSecret = os.getenv('arbitrerSecret')

def initArbitrers():
	arbitre1 = pytactx.Agent("Architecte", "conflicttower", "Damien", arbitrerSecret)
	arbitre1.changerArene("info", "⌛ Initialisation de l'arbitre...")

"""	arbitre2 = pytactx.AgentFr("", "conflicttower", "Gaetan",, url="mqtt.jusdeliens.com")
	arbitre2.changerArene("info", "⌛ Initialisation de l'arbitre...",  url="mqtt.jusdeliens.com")

	arbitre3 = pytactx.AgentFr("", "conflicttower", "Thibaud", "", url="mqtt.jusdeliens.com")
	arbitre3.changerArene("info", "⌛ Initialisation de l'arbitre...")"""


while True:
	initArbitrers()
	
	agent.update()
	agent.lookAt((agent.dir + 1) % 4)