from repo import PlayerRepo
from services import Services
from ui import Console

if __name__ == '__main__':
    repo = PlayerRepo("tenis player.txt")
    service = Services(repo)
    ui = Console(service)

    ui.run()