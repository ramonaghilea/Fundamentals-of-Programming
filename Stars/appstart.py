from board import Board
from game import Game
from ui import UI

b = Board()
g = Game(b)
ui = UI(g)
ui.start()