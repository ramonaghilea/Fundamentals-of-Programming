from repo import Repository

class SentenceException(Exception):
    def __init__(self, msg):
        self._msg = msg

class LetterException(Exception):
    def __init__(self, msg):
        self._msg = msg

class GameOverException(Exception):
    def __init__(self, msg):
        self._msg = msg

class Game:
    def __init__(self, gamesentence):
        self._gamesentence = gamesentence
        #self._gamesentence2 = self.hangman_sentence_init() !!!!!!!! atribute error
        self.correctLetters = []
        self.incorrectLetters = []
        self._hangmanword = "hangman"
        self._hangmanword2 = ""
        self._nr_wrong_letters = 0
        self._gamesentence2 = self.hangman_sentence_init()
        

    def hangman_sentence_init(self):
        firstletter = self._gamesentence[0]
        lastletter = self._gamesentence[-1]
        self.correctLetters.append(firstletter)
        self.correctLetters.append(lastletter)
        hangmanSentence = ""
        for character in self._gamesentence:
            if character == firstletter or character == lastletter or character == " ":
                hangmanSentence += character + " "
            else:
                hangmanSentence += "_ "
        return hangmanSentence

    def propose_letter(self, letter):
        #validate letter
        if len(letter) > 1:
            raise LetterException("Not a letter.")
        if letter >= 'A' and letter <= 'Z':
            letter = letter + ('a' - 'A')
        if not( letter >= 'a' and letter <= 'z'):
            raise LetterException("Not a letter.")

        #self.correctLetters.append(letter)
        result = self.add_letter_to_sentence_or_hangman(letter) #call this function which will decide if the letter
        #is correct or not

        return result

    def add_letter_to_sentence_or_hangman(self, letter):
        # decides whether to add a letter to the sentence or to hangman
        if letter in self.correctLetters or letter in self.incorrectLetters:
            self.add_letter_to_hangman()
            return 0
        elif letter not in self._gamesentence:
            self.incorrectLetters.append(letter)
            self.add_letter_to_hangman()
            return 0
        else:
            self.correctLetters.append(letter)
            self._gamesentence2 = self.add_letter_to_sentence()
            return 1

    def add_letter_to_hangman(self):
        self._nr_wrong_letters += 1
        self._hangmanword2 = self._hangmanword[:self._nr_wrong_letters]
        
    def add_letter_to_sentence(self):
        hangmanSentence = ""
        for character in self._gamesentence:
            if character in self.correctLetters or character == " ":
                hangmanSentence += character
            else:
                hangmanSentence += " _ "
        self._gamesentence2 = hangmanSentence
        return hangmanSentence

    def checkOver(self):
        if " _ " not in self._gamesentence2:
            return True, 1
            #raise GameOverException("You won!!")
        if self._hangmanword == self._hangmanword2:
            return True, 0
            #raise GameOverException("You lost :((")
        return False, None

    def getHangmanWord(self):
        return self._hangmanword2

    def getHangmanSentence(self):
        return self._gamesentence2
        
    def getinitialsentence(self):
        return self._gamesentence