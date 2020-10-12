from board import Board
import copy
import random
import math

class MiniMaxAlgorithm:

    def evaluate_sequence(self, sequence, colour):
        '''
        Evaluates a sequence(list) of 4 consecutive cells.
        If a sequence has 3 'R' (in the case of the AI) and one empty cell, the score will be 5.
        If a sequence has 2 'R' (in the case of the AI) and 2 empty cells, the score will be 2.
        If a sequence has 3 'Y' (the colour of the opponent) and one empty cell, the score will be -4.
        It returns the score of the sequence.
        '''
        if colour == 'R':
            opponent_colour = 'Y'
        else:
            opponent_colour = 'R'

        score = 0
        d = {'Y': 1, 'R': -1}
        value = d[colour]
        opponent_value = d[opponent_colour]

        if sequence.count(value) == 4:
            score += 100
        elif sequence.count(value) == 3 and sequence.count(0) == 1:
            score += 5
        elif sequence.count(value) == 2 and sequence.count(0) == 2:
            score += 2

        if sequence.count(opponent_value) == 3 and sequence.count(0) == 1:
            score -= 4

        return score

    def evaluation_function(self, board, colour):
        '''
        It evaluates the board and returns a score.
        If there are 'R's on the central column, the number of 'R's is multiplied by 3 and added to the score.
        It calls self.evaluate_sequence for every sequence of 4 consecutive cells on every row, then on every column
        and on every diagonal. It adds this sequence score to the global score.
        It returns a global score.
        '''
        score = 0
        d = {'Y': 1, 'R': -1}
        value = d[colour]

        # mark central column if possible
        central_column = []
        for r in range(6):
            central_column.append(board.get(r,3))
        central_score = central_column.count(value)
        score += central_score * 3
        
        # rows
        for r in range(6):
            current_row = []
            for c in range(7):
                current_row.append(board.get(r,c))
            for c in range(5):
                sequence = current_row[c:c+4]
                score += self.evaluate_sequence(sequence, colour)
        # columns
        for c in range(7):
            current_column = []
            for r in range(6):
                current_column.append(board.get(r,c))
            for r in range(4):
                sequence = current_column[r:r+4]
                score += self.evaluate_sequence(sequence, colour)
        
        # secondary diagonals
        for r in range(3,6):
            for c in range(4):
                sequence = []
                for i in range(4):
                    sequence.append(board.get(r-i, c+i))
                score += self.evaluate_sequence(sequence, colour)
        # main diagonals
        for r in range(3,6):
            for c in range(6,2,-1):
                sequence = []
                for i in range(4):
                    sequence.append(board.get(r-i, c-i))
                score += self.evaluate_sequence(sequence, colour)
        
        return score  

    def is_terminal_node(self, board):
        '''
        Returns True if the game is won or the game is tie.
        '''
        return board.isWon('Y') or board.isWon('R') or board.isTie()

    def minimax(self, board, depth, alpha, beta, maximizingPlayer):
        '''
        The computer is the maximizing player and the human is the minimizing player.
        It is a recursive algorithm:
        - If depth is 0, a value is returned.
        - If is_terminal is True, the game is either won or draw and a specific value is returned.
        For every player, it searches for the best column possible, assuming the other player plays optimally.
        
        1. It creates a copy of the current board and simulates every action possible.
        2. It calls self.minimax for the simulated board.
        3. It compares the score returned by the self.minimax to the best value and if this score is greater, replaces
        the previous best value and the previous best column.
        It returns the best column and the best value.
        '''
        valid_positions = board.get_valid_positions()
        is_terminal = self.is_terminal_node(board)

        if depth == 0 or is_terminal:
            if is_terminal:
                if board.isWon('R'):
                    return (None, 1000000000000)
                elif board.isWon('Y'):
                    return (None, -1000000000000)
                else: # game is Tie
                    return (None, 0)
            else:
                return (None, self.evaluation_function(board, 'R'))

        if maximizingPlayer: # the AI, the maximizingPlayer
            value = - math.inf
            column = 0
            for c in valid_positions:
                #row = board.firstFreeSquare(c)
                copy_board = copy.deepcopy(board)
                copy_board.move(c, 'R')
                new_score = self.minimax(copy_board, depth-1, alpha, beta, False)[1]
                if new_score > value:
                    value = new_score
                    column = c
                alpha = max(value, alpha)
                if alpha >= beta:
                    break
            return column, value

        else: # the player, the minimizingPlayer
            value = math.inf
            column = 0
            for c in valid_positions:
                #row = board.firstFreeSquare(c)
                copy_board = copy.deepcopy(board)
                copy_board.move(c, 'Y')
                new_score = self.minimax(copy_board, depth-1, alpha, beta, True)[1]
                if new_score < value:
                    value = new_score
                    column = c
                beta = min(value, beta)
                if alpha >= beta:
                    break
            return column, value