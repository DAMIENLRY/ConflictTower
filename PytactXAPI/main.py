import j2l.pytactx.agent as pytactx

agent = pytactx.Agent(playerId=31012003,
						arena="conflicttower",
						username="demo",
						password="demo",
						server="mqtt.jusdeliens.com",
						verbosity=2)

while True:
	agent.update()
	agent.lookAt((agent.dir + 1) % 4)