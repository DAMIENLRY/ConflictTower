#ADMIN FILE

from res.Arbiter import Arbiter
from dotenv import load_dotenv
from res.troops.ArcherTroop import ArcherTroop
import os

load_dotenv()
arbitrerSecret = os.getenv('arbitrerSecret')

admin = Arbiter(playerId=arbitrerSecret,
                    arena="conflicttower",
                    username="demo",
                    password="demo",
                    server="mqtt.jusdeliens.com",
                    verbosity=2)

ArcherTroop.set_troop_total_health(80)

admin.lunch_game()
