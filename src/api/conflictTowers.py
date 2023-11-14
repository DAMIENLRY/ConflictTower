import j2l.pytactx.agent as pytactx

agent = pytactx.Agent(playerId="31012003",
						arena="conflicttower",
						username="demo",
						password="demo",
						server="mqtt.jusdeliens.com",
						verbosity=2)

def initArbitrers():
	arbitre1 = pytactx.AgentFr("Architecte", "conflicttower", "Damien", "27102003")
	arbitre1.changerArene("info", "⌛ Initialisation de l'arbitre...")

	arbitre2 = pytactx.AgentFr("", "conflicttower", "Gaetan", "31012003")
	arbitre2.changerArene("info", "⌛ Initialisation de l'arbitre...")

	arbitre3 = pytactx.AgentFr("", "conflicttower", "Thibaud", "")
	arbitre3.changerArene("info", "⌛ Initialisation de l'arbitre...")


while True:
	initArbitrers()
	
	agent.update()
	agent.lookAt((agent.dir + 1) % 4)