from texttable import Texttable

class Board:
    #__slots__ = 'a', '__dict__'
    def __init__(self):
        '''
        0 - empty square/circle
        1 - 'Y' yellow
        -1 - 'R' red
        '''
        self._moves = 0
        self._data = [[0]*7, [0]*7, [0]*7, [0]*7, [0]*7, [0]*7] #7 columns and 6 rows

    def get(self, x, y):
        return self._data[x][y]

    def get_valid_positions(self):
        valid_positions = []
        for r in range(6):
            for c in range(7):
                if self._data[r][c] == 0 and (c not in valid_positions):
                    valid_positions.append(c)
        return valid_positions[:]

    def isWon(self, colour):
        '''
        Checks if the game is won (there is a seqence of 4 squares/cirlce of the same colour on a
        row/column/diagonal) and returns True/False.
        '''
        d = {'Y': 1, 'R': -1}
        value = d[colour]
        # horizontal
        for r in range(6):
            for c in range(4):
                if self._data[r][c] == value and abs(self._data[r][c] + self._data[r][c+1] + self._data[r][c+2] + self._data[r][c+3]) == 4:
                    return True
        # vertical
        for c in range(7):
            for r in range(3):
                if self._data[r][c] == value and abs(self._data[r][c] + self._data[r+1][c] + self._data[r+2][c] + self._data[r+3][c]) == 4:
                    return True

        # secondary diagonals
        for r in range(3,6):
            for c in range(4):
                if self._data[r][c] == value and abs(self._data[r][c] + self._data[r-1][c+1] + self._data[r-2][c+2] + self._data[r-3][c+3]) == 4:
                    return True

        # main diagonals
        for r in range(3,6):
            for c in range(6,2,-1):
                if self._data[r][c] == value and abs(self._data[r][c] + self._data[r-1][c-1] + self._data[r-2][c-2] + self._data[r-3][c-3]) == 4:
                    return True

        return False

    def isTie(self):
        '''
        The game is tie if it is not won and there have been 42 moves (all the squares/circles are occupied).
        '''
        return self.isWon('Y') == False and self.isWon('R') == False and self._moves == 42

    def firstFreeSquare(self, column):
        '''
        Takes every square/circle from the bottom to the top of the specific column and returns the first free one.
        Raises an error if the column is full
        '''
        for i in range(5, -1, -1):
            if self._data[i][column] == 0:
                return i
        raise ValueError("Full column")

    def move(self, column, colour):
        '''
        Updates the board after a move: if the player made a move ("Y"), it puts a 1 in that specific place,
        otherwise (the computer makes a move ("R")), it puts a -1.

        Checks if the column and the colour are valid.

        Calls self.firstFreeSquare to find the first free spot in the column.
        '''
        if column not in range(7):
            raise ValueError("Move outside the board")
        if colour not in ['Y', 'R']:
            raise ValueError("Incorrect colour")
        x = self.firstFreeSquare(column)

        d = {'Y': 1, 'R': -1}
        self._data[x][column] = d[colour]
        self._moves += 1

    def put_value(self, column, value):
        x = self.firstFreeSquare(column)
        self._data[x][column] = value
        self._moves += 1

    def copyBoard(self): # a function that copies only the self._data
        aux_board = []
        for r in range(6):
            row = []
            for c in range(7):
                row.append(self._data[r][c])
            aux_board.append(row)
        return aux_board

    def __str__(self):
        t = Texttable()
        d = {0: " ", 1:"Y", -1:"R"}

        for i in range(6):
            row = self._data[i][:]
            for j in range(7):
                row[j] = d[row[j]]
            t.add_row(row)
        return t.draw()