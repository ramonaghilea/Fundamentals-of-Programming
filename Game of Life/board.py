from texttable import Texttable


class BoardError(Exception):
    def __init__(self, msg):
        self._msg = msg


class Board:
    def __init__(self):
        self._data = [[0] * 8, [0] * 8, [0] * 8, [0] * 8, [0] * 8, [0] * 8, [0] * 8, [0] * 8]

    def __str__(self):
        t = Texttable()
        for i in range(0,8):
            row = []
            for j in range(0,8):
                if self._data[i][j] == 0:
                    row.append(' ')
                elif self._data[i][j] == 1:
                    row.append('X')
            t.add_row(row)

        return t.draw()

    def checkEmpty(self, x, y):
        '''
        Checks if the cell of coordinates x, y is empty or not.
        input: -x, y - coordinates
        output: - True - the cell is empty
                - False - the cell is not empty
        '''
        if self._data[x][y] != 0:
            return False
        return True

    def checkInBoard(self, x, y):
        '''
        Checks if the coordinates are inside the board.
        input: - x, y - coordinates
        output: - True - the coordinates are in the board(the cell exists)
                - False - otherwise
        '''
        if x < 0 or x > 7 or y < 0 or y > 7:
            return False
        return True

    def placeCell(self, x, y, symbol):
        elements = {'0': 0, 'X': 1}
        symbol = elements[symbol]
        if self.checkInBoard(x,y):
            self._data[x][y] = symbol
    
    def placePattern(self, pattern, x, y, nrCells):
        '''
        It places a pattern in the board.
        input: - pattern(a list containing the configuration)
            - x, y - the coordinates of the left upper corner of the pattern
            - nrCells - the dimension of the patter (for ex: 3 for a 3x3 pattern)

        output: -
        Raises BoardError if the coordinates of a cell where we want to place a part of the pattern is out of
        the board or if the cell is not empty.
        '''
        elements = {'0': 0, 'X': 1}
        for line in range(nrCells):
            for column in range(nrCells):
                if self.checkInBoard(x+line, y+column) == False and elements[pattern[line][column]] == 1:
                    raise BoardError("Coordinates are outside the board")
                if self.checkEmpty(x+line,y+column) == False and elements[pattern[line][column]] == 1:
                    raise BoardError("A cell is not empty")
                # we can safely put the cell
                if elements[pattern[line][column]] == 1:
                    self._data[x+line][y+column] = elements[pattern[line][column]]

    def getCell(self, x, y):
        '''
        Returns the value in the cell of coordinates x, y.
        input: - x, y = coordinates
        output: - the value in self._data[x][y]
        '''
        return self._data[x][y]

    def getNrNeighbours(self, x, y):
        '''
        Computes the nr of neighbours for a given cell.
        input: - x, y - coordinates
        output: - number of neighbours
        '''
        coordinates = [[-1,-1], [-1,0], [-1,1], [0,-1], [0,1], [1,-1], [1,0], [1,1]]
        nrNeighbours = 0
        for pair in coordinates:
            newx = x + pair[0]
            newy = y + pair[1]

            if self.checkInBoard(newx, newy):
                if self._data[newx][newy] == 1: #the coord are valid and there is a cell
                    nrNeighbours += 1

        return nrNeighbours

    def updateBoard(self, newdata):
        '''
        Updates the board.
        input: - newdata - a list containing the new configuration
        output: -
        '''
        self._data.clear()
        self._data.extend(newdata)

    def getData(self):
        return self._data

