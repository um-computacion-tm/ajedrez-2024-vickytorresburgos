import unittest
from game.piece import Piece
from game.board import Board

class TestPiece(unittest.TestCase):
    def test_SetUp(self):
        piece = Piece("White",self)
        self.assertEqual(piece.__color__,"White")

if __name__ == "__main__":
    unittest.main()
