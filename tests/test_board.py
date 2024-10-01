import unittest
from game.board import Board,OutOfBoard
from game.rook import Rook

class TestBoard(unittest.TestCase):
    def setUp(self):
        self.board = Board(for_test=True)

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
        self.board.place_piece(0, 0, "White")
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


    def test_get_piece_out_of_range(self):
        board = Board(for_test=True)
        with self.assertRaises(OutOfBoard) as exc:
            board.get_piece(10, 10)
        self.assertEqual(
            exc.exception.message,
            "The position selected is out of the board"
        )

    def test_move_piece(self):
            rook = Rook("Black", self.board, 5)
            self.board.place_piece(0, 0, rook)
            self.board.move(0, 0, 1, 1)
            self.assertIsNone(self.board.get_piece(0, 0))
            self.assertEqual(self.board.get_piece(1, 1), rook)

    def test_move_out_of_board(self):
        rook = Rook("Black", self.board, 5)
        self.board.place_piece(0, 0, rook)
        with self.assertRaises(OutOfBoard):
            self.board.move(0, 0, 8, 8)       
        
if __name__ == "__main__":
    unittest.main()
