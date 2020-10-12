from board import Board

class GameExceptionWon(Exception):
    def __init__(self, msg):
        self._msg = msg
class GameExceptionLost(Exception):
    def __init__(self, msg):
        self._msg = msg

class Game:
    def __init__(self, board):
        self._board = board
        self._alienshipsdown = 0

    def fire(self, coordx, coordy):
        #letters = {'A': 1, 'B': 2, 'C': 3, 'D': 4} # THIS SHOULD BE IN BOARD
        cellType = self._board.getCell(coordx, coordy)

        if cellType == 3 and self._alienshipsdown == 1:
            self._board.fire(coordx, coordy)
            raise GameExceptionWon("You won!!")
        
        if cellType == 2 or cellType == 4: # the user can try again, the cell is an asteroid or fired already
            return 0
        elif cellType == 3: # it is an alien ship (the first one)
            self._board.fire(coordx, coordy)
            self._alienshipsdown += 1
            self._board.teleportAlienShip()
            self.checkGameOver() # check if the game is over
            return 1

        elif cellType == 0 or cellType == 10: # empty cell (miss)
            self._board.fire(coordx, coordy)
            self._board.teleportAlienShip()
            self.checkGameOver() # check if the game is over
            return 2

    def getCheatBoard(self):
        return self._board.getCheatBoard()
        
    def checkGameOver(self):
        if self._board.checkEarthAdjacent() == True:
            raise GameExceptionLost("You lost:((")

    def getBoard(self):
        return str(self._board)