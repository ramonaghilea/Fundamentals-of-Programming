from repo import Repository
from service import Service
from ui import UI

repository1 = Repository("sentences.txt")
service1 = Service(repository1)
ui1 = UI(service1)

ui1.start()
