import unittest
from game.piece import Piece

class TestPiece(unittest.TestCase):
    def test_SetUp(self):
        piece = Piece("White")
        self.assertEqual(piece.__color__,"White")

if __name__ == "__main__":
    unittest.main()
