from Tservices import Service
from Trepo import TextFileRepo,TicketTextFileRepo
from Tui import UI

service=Service(TextFileRepo("routes.txt"),TicketTextFileRepo("purchases.txt"))
ui=UI(service)
ui._run()



