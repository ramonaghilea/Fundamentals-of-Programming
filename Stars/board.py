from texttable import Texttable
import random

class Board:
    def __init__(self):
        '''
        Earth = 1
        Asteroid = 2
        Alien ship = 3
        Line (fire) = 4

        adjacent to asteroid = 10
        '''
        self._data = [[0]*7, [0]*7, [0]*7, [0]*7, [0]*7, [0]*7, [0]*7]
        self._aliens = []
        self._niv1 = []
        self._niv2 = []
        self._niv3 = []
        self.configureBoard()
        self.initalizeNiv()

    def getCell(self, x, y):
        letters = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7}
        x = letters[x]
        x -= 1
        y -= 1
        return(self._data[y][x])
    def getAliens(self):
        return self._aliens
    def fire(self, x, y):
        letters = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7}
        x = letters[x]
        x -= 1
        y -= 1
        if self._data[y][x] == 3: # if an alien ship was shot, delete it from self._aliens
            self._aliens.remove([y,x])

        self._data[y][x] = 4
        #self.teleportAlienShip() #change the configuration of alien ships NOT HERE

    def checkEarthAdjacent(self):
        directions = [[1,-1], [1, 0], [1, 1], [-1, -1], [-1, 0], [-1, 1], [0,1], [0, -1]]
        for element in directions:
            newx = 3 + element[0]
            newy = 3 + element[1]
            if self._data[newx][newy] == 3:
                return True
        return False

    def addEarth(self):
        self._data[3][3] = 1

    def addAsteroids(self):
        directions = [[1,-1], [1, 0], [1, 1], [-1, -1], [-1, 0], [-1, 1], [0,1], [0, -1]]

        for i in range(8): # 8 asteroid have to be placed
            freeCells = self.getFreeCells() #list of empty cells (without the neighbours of the other asteroids)

            candidate = random.choice(freeCells) # the cell for the current asteroid
            x = candidate[0]
            y = candidate[1]
            self._data[x][y] = 2 # mark the cell with an asteroid
            # now mark the adjacent cells for future asteroids
            for element in directions:
                newx = x + element[0]
                newy = y + element[1]

                if newx >= 0 and newx < 7 and newy >= 0 and newy < 7 and self._data[newx][newy] == 0:
                    self._data[newx][newy] = 10 # mark the cell as an adjacent cell of an asteroid

    def addAlienShipInitial(self):
        candidatesEqual = []
        for i in range(7):
            if self._data[i][0] == 0 or self._data[i][0] == 10:
                candidatesEqual.append([i,0])
            if self._data[i][6] == 0 or self._data[i][6] == 10:
                candidatesEqual.append([i,6])

        for i in range(1,7):
            if self._data[0][i] == 0 or self._data[0][i] == 10:
                candidatesEqual.append([0,i])
            if self._data[6][i] == 0 or self._data[6][i] == 10:
                candidatesEqual.append([6,i])

        candidateList2 = random.sample(candidatesEqual, 2)
        x1 = candidateList2[0][0]
        y1 = candidateList2[0][1]
        x2 = candidateList2[1][0]
        y2 = candidateList2[1][1]

        self._data[x1][y1] = 3
        self._data[x2][y2] = 3

        self._aliens.append([x1, y1])
        self._aliens.append([x2, y2]) # save the positions of the alien ships

    def initalizeNiv(self):
        niv1 = []
        niv2 = []
        niv3 = []

        # niv1 are the cells at distance 3 from Earth
        for i in range(7):
            niv1.append([i,0])
            niv1.append([i,6])

        for i in range(1,7):
            niv1.append([0,i])
            niv1.append([6,i])

        # niv2 - distance 2
        for i in range(1,6):
            niv2.append([i,1])
            niv2.append([i,5])

        for i in range(2,6):
            niv2.append([1,i])
            niv2.append([5,i])

        # niv3 - distance 1
        for i in range(2,4):
            niv3.append([i,2])
            niv3.append([i,4])

        for i in range(3,4):
            niv3.append([2,i])
            niv3.append([4,i])

        self._niv1 = niv1
        self._niv2 = niv2
        self._niv3 = niv3

        '''
        for element in self._aliens:
            coordx = element[0]
            coordy = element[1]

            candidatesEqual = [] # the list of candidates for equal distance
            for i in range(max(coordx, coordy) + 1):
                if self._data[i][coordy] == 0 or self._data[i][coordy] == 10:
                    candidatesEqual.append([i,coordy])
                if self._data[i][6 - coordy] == 0 or self._data[i][6 - coordy] == 10:
                    candidatesEqual.append([i,6 - coordy])

            for i in range(1,7):
                if self._data[coordx][i] == 0 or self._data[coordx][i] == 10:
                    candidatesEqual.append([coordx ,i])
                if self._data[6 - coordx][i] == 0 or self._data[6 - coordx][i] == 10:
                    candidatesEqual.append([6 - coordx,i])

            candidateEqual = random.choice(candidatesEqual) # the candidate with the same disnance from earth
            
            candidatesEqual = [] # the list of candidates for one cell closer distance
            for i in range(max(coordx, coordy) + 1):
                if self._data[i][coordy] == 0 or self._data[i][coordy] == 10:
                    candidatesEqual.append([i,coordy])
                if self._data[i][6 - coordy] == 0 or self._data[i][6 - coordy] == 10:
                    candidatesEqual.append([i,6 - coordy])

            for i in range(1,7):
                if self._data[coordx][i] == 0 or self._data[coordx][i] == 10:
                    candidatesEqual.append([coordx ,i])
                if self._data[6 - coordx][i] == 0 or self._data[6 - coordx][i] == 10:
                    candidatesEqual.append([6 - coordx,i])
        '''
    def teleportAlienShip(self):
        #self.initalizeNiv()
        newaliens = []
        for element in self._aliens:
            coordx = element[0]
            coordy = element[1]

            candidates = []
            if [coordx, coordy] in self._niv1: # first case, x on the niv1
                # the candidates from the same niv
                candidates = []
                for i in self._niv1:
                    if self._data[i[0]][i[1]] == 0 or self._data[i[0]][i[1]] == 10:
                        candidates.append(i)
                candidateEqual = random.choice(candidates)
                # the candidates from niv closer to Earth
                candidates = []
                for i in self._niv2:
                    if self._data[i[0]][i[1]] == 0 or self._data[i[0]][i[1]] == 10:
                        candidates.append(i)
                candidateCloser = random.choice(candidates)

                candidates = []
                candidates.append(candidateEqual) # in order to have 50% probability
                candidates.append(candidateCloser)

                finalCandidate = random.choice(candidates)

                self._data[coordx][coordy] = 0 # the previous position for 'X' is marked with 0
                self._data[finalCandidate[0]][finalCandidate[1]] = 3
                newaliens.append(finalCandidate)

            else: # second case, x on niv2
                # the candidates from the same niv
                candidates = []
                for i in self._niv2:
                    if self._data[i[0]][i[1]] == 0 or self._data[i[0]][i[1]] == 10:
                        candidates.append(i)
                candidateEqual = random.choice(candidates)
                # the candidates from niv closer to Earth
                candidates = []
                for i in self._niv3:
                    if self._data[i[0]][i[1]] == 0 or self._data[i[0]][i[1]] == 10:
                        candidates.append(i)
                candidateCloser = random.choice(candidates)

                candidates = []
                candidates.append(candidateEqual) # in order to have 50% probability
                candidates.append(candidateCloser)

                finalCandidate = random.choice(candidates)
                
                self._data[coordx][coordy] = 0
                self._data[finalCandidate[0]][finalCandidate[1]] = 3
                newaliens.append(finalCandidate)

        self._aliens = newaliens # the list of aliens is updated


    def configureBoard(self):
        self.addEarth()
        self.addAsteroids()
        self.addAlienShipInitial()

    def getFreeCells(self):
        freeCells = []
        for i in range(7):
            for j in range(7):
                if self._data[i][j] == 0:
                    freeCells.append([i, j])
        return freeCells

    def getCheatBoard(self):
        t = Texttable()
        letters = [' ', 'A', 'B', 'C', 'D', 'E', 'F', 'G']
        symbols = {1: 'E', 2: '*', 3: 'X', 4: '-'}
        t.add_row(letters)

        for i in range(7):
            row = []
            row.append(i+1)
            for j in range(7):
                if self._data[i][j] in symbols:
                    row.append(symbols[self._data[i][j]])
                else:
                    row.append(' ')
            t.add_row(row)
        return(t.draw())

    def __str__(self):
        t = Texttable()
        letters = [' ', 'A', 'B', 'C', 'D', 'E', 'F', 'G']
        #symbols = {1: 'E', 2: '*', 3: 'X', 4: '-'}
        t.add_row(letters)

        for i in range(7):
            row = []
            row.append(i+1)
            for j in range(7):
                if i == j == 3:
                    row.append('E')
                else:
                    row.append(' ')
            t.add_row(row)
        return(t.draw())
