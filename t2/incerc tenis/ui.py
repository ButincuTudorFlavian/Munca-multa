from services import Services

class Console:
    def __init__(self, service):
        self._service = service

    def run(self):
        while True:
            print("\n1. Display strenght descending")
            print("x. Exit")

            cmd = input("Select option: ")

            if cmd == "1":
                lista_jucatori = self._service.list_all_for_strenght_descending()
                if not lista_jucatori:
                    print("No players found")
                else:
                    for player in lista_jucatori:
                        print(player)

            elif cmd == "x":
                break

            else:
                print("Invalid input")