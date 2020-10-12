from repo import Repository
import random

class SentenceException(Exception):
    def __init__(self, msg):
        self._msg = msg

class LetterException(Exception):
    def __init__(self, msg):
        self._msg = msg

class GameOverException(Exception):
    def __init__(self, msg):
        self._msg = msg

class Service:
    def __init__(self, repo):
        self._repo = repo
    
    def add_sentence(self, sentence):
        '''
        The method add_sentence(sentence) calls self._repo.add_sentence, which adds the sentence in the repo.
        input: - sentence (a string)
        output: -
        - raises SentenceException if the sentence has no word or if there is at least a word with less than
        3 letters
        '''
        sentence2 = sentence.split(" ")
        if sentence2 == ['']:
            raise SentenceException("The sentence has no word")
        for word in sentence2:
            if len(word) < 3:
                raise SentenceException("There is a word with less than 3 letters")

        self._repo.add_sentence(sentence)

    def select_sentence_for_game(self):
        newsentence = random.choice(self._repo.getAll())
        return newsentence

    def getAll(self):
        return self._repo
