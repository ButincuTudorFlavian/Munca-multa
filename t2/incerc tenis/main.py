from domain import *
from repo import *
from services import *
from ui import *

if __name__ == '__main__':
    playerrepo = PlayerRepo("tenis player.txt")
    service = Services(playerrepo)
    ui = Console(service)

    ui.run()