from board import Board
from algorithm_minimax import MiniMaxAlgorithm
import math

class GameWonException(Exception):
    def __init__(self, msg):
        super().__init__(msg)
class GameDrawException(Exception):
    def __init__(self, msg):
        super().__init__(msg)

class Game:
    def __init__(self, board, algorithm):
        self._board = board
        self._algorithm = algorithm

    def playerMove(self, column):
        '''
        Calls self._board.move with the chosen column and the "Y" parameter (when the player makes a move).
        '''
        self._board.move(column, 'Y')

    def computerMove(self):
        '''
        Calls self._algorithm.minimax in order to find the move of the computer.
        Calls self._board.move with the chosen column and the "R" parameter (when the computer makes a move).
        '''
        column = self._algorithm.minimax(self._board, 3, -math.inf, math.inf, True)[0]
        # this must not raise exceptions
        self._board.move(column, 'R')
    
    def check(self):
        '''
        Checks if the game is won or tie.
        Calls self._board.isWon('Y') and if it is True, raises the GameWonError.
        Calls self._board.isWon('R') and if it is True, raises the GameWonError.
        Calls self._board.isTie() and if it is True, raises the GameDrawError.
        '''
        if self._board.isWon('Y') == True or self._board.isWon('R') == True:
            raise GameWonException("")
        if self._board.isTie() == True:
            raise GameDrawException("")

    def getBoard(self):
        return self._board