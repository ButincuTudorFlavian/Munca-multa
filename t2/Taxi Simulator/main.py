from repository import TaxiRepository
from services import TaxiService
from ui import ConsoleUI

def main():
    repo = TaxiRepository()
    service = TaxiService(repo)

    ui = ConsoleUI(service)
    ui.start()

if __name__ == "__main__":
    main()