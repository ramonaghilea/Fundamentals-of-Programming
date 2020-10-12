from game import Game
from game import GameWonException, GameDrawException

class UI:
    def __init__(self, game):
        self._game = game

    def _readPLayerMove(self):
        cmd = input("Give column:")
        return int(cmd)

    def start(self):
        board = self._game.getBoard()

        playerMove = True

        while True:
            print("Enter -1 to exit")
            print(board)

            try:
                
                if playerMove == True:
                    column = self._readPLayerMove()
                    if column == -1:
                        return
                    else:
                        self._game.playerMove(column)
                        self._game.check()
                else:
                    self._game.computerMove()
                    self._game.check()

                playerMove = not playerMove

            except GameWonException:
                print(board)
                if playerMove == True:
                    print("Congrats!")
                else:
                    print("You were defeated")
                return
            except GameDrawException:
                print(board)
                print("Game is draw!")
                return
            except ValueError as er:
                print(str(er))
                continue
