from board import Board
from algorithm_minimax import MiniMaxAlgorithm
from game import Game
from game import GameWonException, GameDrawException
import unittest
import copy
import math
from texttable import Texttable

class TestConnectFour(unittest.TestCase):
    def testBoard_copy(self):
        b = Board()
        b2 = copy.copy(b)
        self.assertEqual(b, b2)
        #assertIsInstance

    def testBoard_get(self):
        b = Board()
        b.move(5, 'Y')
        b.move(5, 'R')
        pos1 = b.get(0,5)
        pos2 = b.get(1,5)
        self.assertEqual(pos1, 1)
        self.assertEqual(pos2, -1)

    def testBoard_get_valid_positions(self):
        b = Board()
        valid_pos = b.get_valid_positions()
        valid_pos_2 = []
        for c in range(7):
            valid_pos_2.append(c)
        self.assertEqual(valid_pos, valid_pos_2)
    
    def testBoard_isWon(self):
        b = Board()
        self.assertFalse(b.isWon('Y'))
        b.move(5, 'Y')
        b.move(4, 'Y')
        b.move(3, 'Y')
        b.move(2, 'Y')
        self.assertTrue(b.isWon('Y'))

    def testBoard_iTie(self):
        b = Board()
        self.assertFalse(b.isTie())

    def testBoard_firstFreeSquare(self):
        b = Board()
        self.assertEqual(b.firstFreeSquare(2), 0)
        b.move(2, 'Y')
        self.assertEqual(b.firstFreeSquare(2), 1)

    def testBoard_move(self):
        b = Board()
        b.move(4, 'Y')
        self.assertEqual(b.get(4, 0), 1)
        self.assertRaises(ValueError, b.move, 9, 'Y')
        self.assertRaises(ValueError, b.move, 3, 'H')

    def testAlgorithm_evaluate_sequence(self):
        alg = MiniMaxAlgorithm()
        sequence = [1, 1, 1, 0]
        self.assertEqual(alg.evaluate_sequence(sequence, 'Y'), 5)
        self.assertEqual(alg.evaluate_sequence(sequence, 'R'), -4)

    def testAlgorithm_evaluation_function(self):
        b = Board()
        alg = MiniMaxAlgorithm()
        b.move(0, 'Y')
        b.move(1, 'Y') # 1 1 1 0 (horizontal)
        b.move(2, 'Y')

        b.move(0, 'Y')
        b.move(0, 'Y') # 1 1 1 0 (vertical)
        
        self.assertEqual(alg.evaluation_function(b, 'Y'), 10)

    def testAlgorithm_is_terminal_node(self):
        b = Board()
        alg = MiniMaxAlgorithm()
        b.move(0, 'Y')
        b.move(1, 'Y') # 1 1 1 0 (horizontal)
        b.move(2, 'Y')
        b.move(3, 'Y')
        self.assertTrue(alg.is_terminal_node(b))

    def testAlgorithm_minimax(self):
        b = Board()
        alg = MiniMaxAlgorithm()
        b.move(0, 'R')
        b.move(2, 'R')
        b.move(3, 'R')

        self.assertEqual(alg.minimax(b, 2, -math.inf, math.inf, True)[0], 1)
    
    def testGame_playerMove(self):
        b = Board()
        alg = MiniMaxAlgorithm()
        g = Game(b, alg)
        g.playerMove(3)
        self.assertEqual(b.get(0, 3), 1)

    def testGame_computerMove(self):
        b = Board()
        alg = MiniMaxAlgorithm()
        g = Game(b, alg)
        g.playerMove(3)
        g.computerMove()
        self.assertEqual(b.get(1, 3), -1)
    
    def testGame_check(self):
        b = Board()
        alg = MiniMaxAlgorithm()
        g = Game(b, alg)
        
        b.move(0, 'R')
        b.move(1, 'R')
        b.move(2, 'R')
        b.move(3, 'R')
        self.assertRaises(GameWonException, g.check)

        for c in range(7):
            for r in range(6):
                b.move(c, 'Y')
        self.assertRaises(GameDrawException, g.check)
    
    def testGame_getBoard(self):
        b = Board()
        alg = MiniMaxAlgorithm()
        g = Game(b, alg)
        b2 = g.getBoard()
        self.assertEqual(b, b2)

if __name__ == '__main__':
    unittest.main()

