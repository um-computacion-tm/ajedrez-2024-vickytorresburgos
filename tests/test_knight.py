import unittest

from game.board import Board
from game.knight import Knight

class TestKnight(unittest.TestCase):
    def setUp(self):
        self.board = Board(for_test=True)
        self.white_knight = Knight(color='White', board=self.board, score=3)
        self.black_knight = Knight(color='Black', board=self.board, score=3)
        self.board.place_piece(1, 0, self.white_knight)
        self.board.place_piece(6, 0, self.black_knight)
    
    def test_white_str(self):
        self.assertEqual(self.white_knight.white_str(), "♘")

    def test_black_str(self):
        self.assertEqual(self.black_knight.black_str(), "♞")

    def test_white_knight_possible_positions(self):
        possibles = self.white_knight.possible_positions(1, 0, [(-2, 1), (-2, -1), (2, 1), (2, -1), (1, 2), (-1, 2), (1, -2), (-1, -2)], False)
        expected = [(3, 1), (2, 2), (0 ,2)]
        self.assertEqual(possibles, expected)

    def test_black_knight_possible_positions(self):
        possibles = self.black_knight.possible_positions(6, 0, [(-2, 1), (-2, -1), (2, 1), (2, -1), (1, 2), (-1, 2), (1, -2), (-1, -2)], False)
        expected = [(4, 1), (7, 2), (5, 2)]
        self.assertEqual(possibles, expected)

if __name__ == '__main__':
    unittest.main()
        