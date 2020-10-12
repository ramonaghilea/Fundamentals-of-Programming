from board import Board, BoardError

class Service:
    def __init__(self, board):
        self._board = board

    def getBoard(self):
        return str(self._board)

    def loadCellPattern(self, name):
        '''
        Loads the textfile name.txt (a cell pattern) and returns a list containg the elements.
        input: the file name
        output: pattern = a list containing the configuration in the file
        '''
        pattern = []
        if name == '':
            pass
        else:
            name = name + '.txt'
            f = open(name, 'r')
            line = f.readline().strip()

            while len(line) > 0:
                line = line.split(' ') # list of elements
                pattern.append(line)
                line = f.readline().strip()

            f.close()

            return pattern

    def placePattern(self, name, x, y):
        '''
        First, it calls self.loafCellPattern in order to get the specific pattern.
        Places a pattern in board.
        input: - filename, coordinates of the upper left corner of the pattern in board(where it should be put)
        output: -
        '''
        pattern = self.loadCellPattern(name) #load the pattern from file
        if name == 'blinker':
            self._board.placePattern(pattern, x, y, 3)
        elif name == 'block':
            self._board.placePattern(pattern,x,y,2)
        elif name == 'tub':
            self._board.placePattern(pattern,x,y,3)
        elif name == 'beacon':
            self._board.placePattern(pattern,x,y,4)
        else:
            numberRows = len(pattern)
            self._board.placePattern(pattern, x, y, numberRows)

    def onetick(self):
        '''
        Creates a generations and updates the board.
        input: -
        output: -
        '''
        newdata = [[0] * 8, [0] * 8, [0] * 8, [0] * 8, [0] * 8, [0] * 8, [0] * 8, [0] * 8]
        for i in range(8):
            for j in range(8):
                if self._board.getCell(i,j) == 0: #dead cell
                    nrNeighbours = self._board.getNrNeighbours(i,j)
                    if nrNeighbours == 3: #the cell becomes a live cell
                        newdata[i][j] = 1
                    
                else: #live cell
                    nrNeighbours = self._board.getNrNeighbours(i,j)
                    if nrNeighbours < 2: #underpopulation, cell dies
                        newdata[i][j] = 0
                    elif nrNeighbours == 2 or nrNeighbours == 3: # remains a live cell
                        newdata[i][j] = 1
        self._board.updateBoard(newdata)

    def tick(self, number):
        '''
        Creates number generations.
        It calls self.onetick() for number times.
        input: - number - integer representing the number of generations
        output: -
        '''
        for i in range(number):
            self.onetick()

    def saveFile(self, name):
        elements = {0: '0', 1: 'X'}
        name = name + '.txt'
        f = open(name, 'w')
        config = ''
        for i in range(8):
            line = ''
            for j in range(8):
                cell = self._board.getCell(i,j)
                line = line + elements[cell] + ' '
            config += line + '\n'

        f.write(config)
        f.close()

    def loadFile(self, name):
        elements = {'0': 0, 'X': 1}
        name = name + '.txt'
        f = open(name, 'r')
        line = f.readline().strip()
        nr = 0
        result = []
        while len(line) > 0:
            nr += 1
            line = line.split(' ') # list of elements
            result.append(line)
            line = f.readline().strip()

        for i in range(nr):
            for j in range(nr):
                result[i][j] = elements[result[i][j]]

        self._board.updateBoard(result)

        f.close()

    def getData(self):
        return self._board.getData()
