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
        self.assertIsNone(self.board.get_piece(2, 2))
        self.assertIsNone(self.board.get_piece(3, 3))
        self.assertIsNone(self.board.get_piece(4, 4))

    def test_place_piece(self):
        self.board.place_piece(0, 0, "White")  # Cambiado el orden
        self.assertIsInstance(self.board.get_piece(0, 0), str)
        self.board.place_piece(0, 7, "White")
        self.assertIsInstance(self.board.get_piece(0, 7), str)
        self.board.place_piece(7, 0, "Black")
        self.assertIsInstance(self.board.get_piece(7, 0), str)
        self.board.place_piece(7, 7, "Black")
        self.assertIsInstance(self.board.get_piece(7, 7), str)
        
        
    def test_str_board(self):
        board = Board()
        self.assertEqual(
            str(board),
            (
                "♜ ♞ ♝ ♛ ♚ ♝ ♞ ♜ \n"
                "♟ ♟ ♟ ♟ ♟ ♟ ♟ ♟ \n"
                "                \n"
                "                \n"
                "                \n"
                "                \n"
                "♙ ♙ ♙ ♙ ♙ ♙ ♙ ♙ \n"
                "♖ ♘ ♗ ♕ ♔ ♗ ♘ ♖ \n"
            )
        )

        
if __name__ == "__main__":
    unittest.main()
