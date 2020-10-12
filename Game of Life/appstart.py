from board import Board
from service import Service
from ui import UI

newBoard = Board()
newService = Service(newBoard)
newUi = UI(newService)

newUi.start()