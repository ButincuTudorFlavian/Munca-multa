from repository import PlayerRepository
from services import TournamentServices
from ui import ConsoleUI

def main():
    repo = PlayerRepository("players.txt")

    service = TournamentServices(repo)

    ui = ConsoleUI(service)
    ui.start()

if __name__ == "__main__":
    main()