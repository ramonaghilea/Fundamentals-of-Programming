from board import Board
from algorithm_minimax import MiniMaxAlgorithm
from game import Game
from ui import UI
from gui import GUI


board = Board()
alg = MiniMaxAlgorithm()
game = Game(board, alg)
gui = GUI(game)
gui.start()