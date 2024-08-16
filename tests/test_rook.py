import unittest
from game.board import Board
from game.rook import Rook

class TestRook(unittest.TestCase):
    def setUp(self):
        self.board = Board()
        # self.rook = Rook(self)
        # self.board.place_piece(self.rook, 0, 0)

    # def test_valid_move_horizontal(self):
    #     self.assertTrue(self.rook.valid_move(0, 0, 0, 5, self.board))

    # def test_valid_move_vertical(self):
    #     self.assertTrue(self.rook.valid_move(0, 0, 5, 0, self.board))

    # def test_invalid_move_diagonal(self):
    #     self.assertFalse(self.rook.valid_move(0, 0, 5, 5, self.board))

if __name__ == "__main__":
    unittest.main()
