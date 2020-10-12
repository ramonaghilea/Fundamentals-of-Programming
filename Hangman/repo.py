from copy import deepcopy

class DuplicateException(Exception):
    def __init__(self, msg):
        self._msg = msg

class Repository:
    def __init__(self, filename):
        self._sentences = []
        self._filename = filename
        self._loadfile()

    def _loadfile(self):
        f = open(self._filename, 'r')
        
        line = f.readline().strip()
        while len(line) > 0:
            self._sentences.append(line)
            line = f.readline().strip()
        f.close()

    def writeFile(self):
        f = open(self._filename, 'w')
        for sentence in self._sentences:
            res = ""
            res = sentence + "\n"
            f.write(res)
        f.close()

    def add_sentence(self, sentence):
        '''
        The method add_sentence(sentence) adds a sentence to the repo and stores it in the textfile.
        input: - sentence(string)
        output: - 
        - raises DuplicateException() if an identical sentence is already stored in the repo
        '''
        self._sentences = []
        self._loadfile()

        for s in self._sentences:
            if s == sentence:
                raise DuplicateException("The sentence already exists")
        self._sentences.append(sentence)
        self.writeFile()
    
    def getAll(self):
        self._sentences = []
        self._loadfile()
        return self._sentences[:]
        

    def getSentenceByIndex(self, idx):
        self._sentences = []
        self._loadfile()
        return self._sentences[idx]
        
