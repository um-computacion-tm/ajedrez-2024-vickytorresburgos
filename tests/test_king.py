import unittest

from game.board import Board
from game.king import King

class TestKing(unittest.TestCase):
    def setUp(self):
        self.board = Board(for_test=True)
        self.white_king = King(color='White', board=self.board, score=1)
        self.black_king = King(color='Black', board=self.board, score=1)
        self.board.place_piece(1, 0, self.white_king)
        self.board.place_piece(6, 0, self.black_king)
    
    def test_white_str(self):
        self.assertEqual(self.white_king.white_str(), "♔")

    def test_black_str(self):
        self.assertEqual(self.black_king.black_str(), "♚")
        
    def test_king_possible_positions(self):
        possibles = self.white_king.possible_positions(1, 0, [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, 1), (-1, -1), (1, 1), (1, -1)], False)
        expected = [(0, 0), (2, 0), (1, 1), (0, 1), (2, 1)]
        self.assertEqual(possibles, expected)

    def test_king_possible_positions(self):
        possibles = self.black_king.possible_positions(6, 0, [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, 1), (-1, -1), (1, 1), (1, -1)], False)
        expected = [(5, 0), (7, 0), (6, 1), (5, 1), (7, 1)]
        self.assertEqual(possibles, expected)
    

if __name__ == '__main__':
    unittest.main()
    