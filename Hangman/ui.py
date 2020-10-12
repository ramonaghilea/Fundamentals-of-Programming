from service import Service
from game import Game
class UI:
    def __init__(self, service):
        self._service = service

    def printMenu(self):
        res = ""
        res += "0. Exit \n"
        res += "1. Add a sentence. \n"
        res += "2. Start game. \n"

        print(res)

    def start_game_ui(self):
        gamesentence = self._service.select_sentence_for_game()
        
        #print(gamesentence)
        game = Game(gamesentence) # initialize game

        isgameOn = True
        while isgameOn:
            try:
                print(game.getHangmanSentence())
                letter = input("Give letter: ")
                try:
                    result = game.propose_letter(letter)
                    if result == 1: # the letter was ok
                        #print(game.getHangmanSentence())
                        pass
                    else:
                        print(game.getHangmanWord())
                except Exception as ex:
                    print(ex)
                isgameOn, res = game.checkOver()
                isgameOn = not isgameOn
                if res == 1:
                    print("you won!!")
                elif res == 0:
                    print("you lost:((")
                    print("The sentence was <<", game.getinitialsentence(), ">>")
            except Exception as er:
                print(er)

        #hangmansentence = self.game.hangman_sentence_init(gamesentence)

    def add_sentence_ui(self):
        sentence = input("Give sentence: ")
        self._service.add_sentence(sentence)

    def start(self):
        commands = {"1": self.add_sentence_ui, "2": self.start_game_ui}

        while True:
            try:

                self.printMenu()
                cmd = input("Enter command: ")

                if cmd == "0":
                    return
                elif cmd in commands:
                    commands[cmd]()
            except Exception as ex:
                print(ex)