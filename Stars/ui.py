from game import Game, GameExceptionWon, GameExceptionLost

class UI:
    def __init__(self, game):
        self._game = game

    def _printMenu(self):
        res = "Commands:"
        res += "exit \n"
        res += "fire <coordinate> \n"
        res += "cheat \n"

        return res

    def start(self):
        cmd2 = ""
        gameOn = True
        while gameOn:
            try:
                self._printMenu()
                if cmd2 != "cheat":
                    print(self._game.getBoard())
                cmd2 = input("Enter command: ")

                if cmd2 == 'exit':
                    return
                if cmd2 == 'cheat':
                    print(self._game.getCheatBoard())
                else:
                    cmd = cmd2.split()
                    if cmd[0] == 'fire':
                        result = self._game.fire(cmd[1][0], int(cmd[1][1]))
                        if result == 0:
                            print("Try again. The cell was an asteroid or was previously fired upon.")

                            while result == 0:
                                cmd = input("Enter a valid cell: ")
                                cmd = cmd.split()
                                result = self._game.fire(cmd[1][0], int(cmd[1][1]))
                                if result == 1:
                                    print("Hit. You fired one alien ship.")
                                elif result == 2:
                                    print("The cell was empty.")

                        elif result == 1:
                            print("Hit. You fired one alien ship.")
                        elif result == 2:
                            print("The cell was empty.")
                        #self._game.checkGameOver()
                    else:
                        print("Bad Command")
                
            except GameExceptionWon as ex:
                print(self._game.getCheatBoard())
                print(ex)
                gameOn = False
            except GameExceptionLost as ex:
                print(self._game.getCheatBoard())
                print(ex)
                gameOn = False