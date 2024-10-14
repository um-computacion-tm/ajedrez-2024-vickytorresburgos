import unittest

from game.board import Board
from game.queen import Queen

class TestQueen(unittest.TestCase):
    def setUp(self):
        self.board = Board(for_test=True)
        self.white_queen = Queen(color='White', board=self.board, score=9)
        self.black_queen = Queen(color='Black', board=self.board, score=9)
        self.board.place_piece(1, 0, self.white_queen)
        self.board.place_piece(6, 0, self.black_queen)

    def test_white_str(self):
        self.assertEqual(self.white_queen.white_str(), "♕")

    def test_black_str(self):
        self.assertEqual(self.black_queen.black_str(), "♛")

    def test_white_queen_possible_positions(self):
        possibles = self.white_queen.possible_positions(1, 0 , [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, 1), (-1, -1), (1, 1), (1, -1)], True)
        expected =[(0, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0), (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (0, 1), (2, 1), (3, 2), (4, 3), (5, 4), (6, 5), (7, 6)]
        self.assertEqual(possibles, expected)

    def test_black_queen_possible_positions(self):
        possibles = self.black_queen.possible_positions(6, 0, [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, 1), (-1, -1), (1, 1), (1, -1)], True)
        expected = [(5, 0), (4, 0), (3, 0), (2, 0), (1, 0), (0, 0), (7, 0), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5), (6, 6), (6, 7), (5, 1), (4, 2), (3, 3), (2, 4), (1, 5), (0, 6), (7, 1)]
        self.assertEqual(possibles, expected)

if __name__ == '__main__':
    unittest.main()
