from board import Board

import random
class MoveAlgorithm:
    # take the first unocupied square
    def nextMove(self, board):
        # Return the computers next move
        candidates = []
        for i in range(6):
            for j in range(7):
                if board.get(i,j) == 0:
                    candidates.append((i,j))
        choice = random.choice(candidates)
        return choice[1]