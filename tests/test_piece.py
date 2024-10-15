import unittest
from game.piece import Piece

class TestPiece(unittest.TestCase):
    def setUp(self):
        self.board = None  
        self.white_piece = Piece("White", self.board, 1)
        self.black_piece = Piece("Black", self.board, 2)

    def test_initialization(self):
        self.assertEqual(self.white_piece.color, "White")
        self.assertEqual(self.white_piece.score, 1)
        self.assertEqual(self.black_piece.color, "Black")
        self.assertEqual(self.black_piece.score, 2)

    def test_str_representation(self):
        self.assertEqual(str(self.white_piece), "")  
        self.assertEqual(str(self.black_piece), "")  

    def test_get_color(self):
        self.assertEqual(self.white_piece.color, "White")
        self.assertEqual(self.black_piece.color, "Black")

    def test_get_score(self):
        self.assertEqual(self.white_piece.score, 1)
        self.assertEqual(self.black_piece.score, 2)


if __name__ == "__main__":
    unittest.main()
