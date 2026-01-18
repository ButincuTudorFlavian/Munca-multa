from Hrepo import TextFileRepo
from Hservices import Service
from Hui import UI

service=Service(TextFileRepo("sentences.txt"))
ui=UI(service)
ui._run()