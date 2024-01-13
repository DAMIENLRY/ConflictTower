#ADMIN FILE

from res.Arbiter import Arbiter
from dotenv import load_dotenv
import os

load_dotenv()
arbitrerSecret = os.getenv('arbitrerSecret')

admin = Arbiter(playerId=arbitrerSecret,
                    arena="conflicttower",
                    username="demo",
                    password="demo",
                    server="mqtt.jusdeliens.com",
                    verbosity=2)

if admin.can_start_game():
    admin.lunch_game()
