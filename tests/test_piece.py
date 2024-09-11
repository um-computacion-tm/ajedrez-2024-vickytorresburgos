import unittest
from game.piece import Piece

class TestPiece(unittest.TestCase):
    def test_SetUp(self):
        piece = Piece("White",self)
        self.assertEqual(piece.__color__,"White")

    def test_white_str(self):
        piece = Piece("White",self)
        self.assertEqual(str(piece),"")

    def test_black_str(self):
        piece = Piece("Black",self)
        self.assertEqual(str(piece),"")

if __name__ == "__main__":
    unittest.main()
