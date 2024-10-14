import unittest
from game.chess import Chess
from game.board import Board
from game.exceptions import OutOfBoard
from game.king import King
from game.rook import Rook

class TestBoard(unittest.TestCase):
    def setUp(self):
        self.board = Board()
        chess = Chess()

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
                "    1   2   3   4   5   6   7   8\n"
                "  ┌───┬───┬───┬───┬───┬───┬───┬───┐\n"
                "1 │ ♜ │ ♞ │ ♝ │ ♛ │ ♚ │ ♝ │ ♞ │ ♜ │ \n" 
                "  ├───┼───┼───┼───┼───┼───┼───┼───┤\n"
                "2 │ ♟ │ ♟ │ ♟ │ ♟ │ ♟ │ ♟ │ ♟ │ ♟ │ \n" 
                "  ├───┼───┼───┼───┼───┼───┼───┼───┤\n"
                "3 │   │   │   │   │   │   │   │   │ \n"
                "  ├───┼───┼───┼───┼───┼───┼───┼───┤\n"
                "4 │   │   │   │   │   │   │   │   │ \n" 
                "  ├───┼───┼───┼───┼───┼───┼───┼───┤\n"
                "5 │   │   │   │   │   │   │   │   │ \n"
                "  ├───┼───┼───┼───┼───┼───┼───┼───┤\n"
                "6 │   │   │   │   │   │   │   │   │ \n"
                "  ├───┼───┼───┼───┼───┼───┼───┼───┤\n"
                "7 │ ♙ │ ♙ │ ♙ │ ♙ │ ♙ │ ♙ │ ♙ │ ♙ │ \n" 
                "  ├───┼───┼───┼───┼───┼───┼───┼───┤\n"
                "8 │ ♖ │ ♘ │ ♗ │ ♕ │ ♔ │ ♗ │ ♘ │ ♖ │ \n" 
                "  └───┴───┴───┴───┴───┴───┴───┴───┘"
            )
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

    def test_place_piece(self):
        piece = King("White", self.board, 0)
        self.board.place_piece(0, 0, piece)
        placed_piece = self.board.get_piece(0, 0)
        self.assertIsNotNone(placed_piece)
        self.assertEqual(placed_piece, piece)

if __name__ == "__main__":
    unittest.main()
