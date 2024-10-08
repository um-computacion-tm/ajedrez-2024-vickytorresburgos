import unittest
from game.chess import Chess
from game.board import Board
from game.exceptions import OutOfBoard
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
        chess = Chess()
        chess.__board__.place_piece(0, 0, Rook("Black", self.board, 5))
        with self.assertRaises(OutOfBoard):
            chess.validate_move(0, 0, 8, 8) 

    def test_place_piece_valid_position(self):
        rook = Rook(color='white', board=self.board, score=5)  
        self.board.place_piece(0, 0, rook)  
        self.assertEqual(self.board.get_piece(0, 0), rook)  

    def test_place_piece_invalid_position(self):
        rook = Rook(color='white', board=self.board, score=5)
        
        with self.assertRaises(OutOfBoard):  
            self.board.place_piece(-1, 0, rook)  

        with self.assertRaises(OutOfBoard):  
            self.board.place_piece(8, 8, rook)  

        with self.assertRaises(OutOfBoard):  
            self.board.place_piece(0, -1, rook)  

        with self.assertRaises(OutOfBoard):  
            self.board.place_piece(0, 8, rook) 
        
if __name__ == "__main__":
    unittest.main()
