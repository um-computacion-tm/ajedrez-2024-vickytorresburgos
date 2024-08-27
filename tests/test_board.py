import unittest
from game.board import Board
from game.rook import Rook

class TestBoard(unittest.TestCase):
    def setUp(self):
        self.board = Board()

    def test_initial_position(self):
        self.assertIsInstance(self.board.get_piece(0, 0), Rook) 
        self.assertIsInstance(self.board.get_piece(0, 7), Rook)
        self.assertIsInstance(self.board.get_piece(7, 0), Rook)
        self.assertIsInstance(self.board.get_piece(7, 7), Rook)

    def test_empty_positions(self):
        self.assertIsNone(self.board.get_piece(1, 1))
        self.assertIsNone(self.board.get_piece(6, 6))
        self.assertIsNone(self.board.get_piece(4, 4))

    def test_place_piece(self):
        self.board.place_piece("White",0,0)
        self.assertIsInstance(self.board.get_piece(0, 0), str)
        self.board.place_piece("White", 0, 7)
        self.assertIsInstance(self.board.get_piece(0, 7), str)
        self.board.place_piece("Black", 7, 0)
        self.assertIsInstance(self.board.get_piece(7, 0), str)
        self.board.place_piece("Black", 7, 7)
        



 
if __name__ == "__main__":
    unittest.main()
