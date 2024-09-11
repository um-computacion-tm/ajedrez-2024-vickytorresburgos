import unittest
from game.board import Board
from game.rook import Rook
from game.pawn import Pawn

class TestRook(unittest.TestCase):
    
    def setUp(self):
        self.board = Board()
        self.rook = Rook(self.board, 'white')

    def test_str_white(self):
        rook = Rook('White', self)
        self.assertEqual(rook.white_str(), '♖')

    def test_black_str(self):
        rook = Rook('Black', self)
        self.assertEqual(rook.black_str(), '♜')


    def test_move_vertical_desc_empty(self):
        board = Board(for_test=True)
        rook = Rook("White", board)
        board.place_piece(4, 4, rook)  
        possibles = rook.possible_positions_vd(4, 4)
        self.assertEqual(possibles,[(5, 4), (6, 4), (7, 4)])

    def test_move_vertical_desc_opponent(self):
        board = Board(for_test=True)
        rook = Rook("White", board)
        board.place_piece(4, 4, rook)  
        opponent_piece = Pawn("Black", board)
        board.place_piece(5, 4, opponent_piece)  
        possibles = rook.possible_positions_vd(4, 4)
        self.assertEqual(possibles,[(5, 4)])

    def test_move_vertical_desc_ally(self):
        board = Board(for_test=True)
        rook = Rook("White", board)
        board.place_piece(4, 4, rook)  
        ally_piece = Pawn("White", board)
        board.place_piece(5, 4, ally_piece)  
        possibles = rook.possible_positions_vd(4, 4)
        self.assertEqual(possibles,[])

    def test_move_vertical_asc_empty(self):
        board = Board(for_test=True)
        rook = Rook("White", board)
        board.place_piece(4, 4, rook)  
        possibles = rook.possible_positions_va(4, 4)
        self.assertEqual(possibles,[(3, 4), (2, 4), (1, 4), (0, 4)]
        )

    def test_move_vertical_asc_opponent(self):
        board = Board(for_test=True)
        rook = Rook("White", board)
        board.place_piece(4, 4, rook)  
        opponent_piece = Pawn("Black", board)
        board.place_piece(3, 4, opponent_piece) 
        possibles = rook.possible_positions_va(4, 4)
        self.assertEqual(
            possibles,
            [(3, 4)]
        )

    def test_move_vertical_asc_ally(self):
        board = Board(for_test=True)
        rook = Rook("White", board)
        board.place_piece(4, 4, rook)  
        ally_piece = Pawn("White", board)
        board.place_piece(3, 4, ally_piece) 
        possibles = rook.possible_positions_va(4, 4)
        self.assertEqual(
            possibles,
            []
        )

    def test_move_horizontal_left_empty(self):
        board = Board(for_test=True)
        rook = Rook("White", board)
        board.place_piece(4, 4, rook)  
        possibles = rook.possible_positions_hl(4, 4)
        self.assertEqual(
            possibles,
            [(4, 5), (4, 6), (4, 7)]
        )

    def test_move_horizontal_left_opponent(self):
        board = Board(for_test=True)
        rook = Rook("White", board)
        board.place_piece(4, 4, rook)  
        opponent_piece = Pawn("Black", board)
        board.place_piece(4, 5, opponent_piece) 
        possibles = rook.possible_positions_hl(4, 4)
        self.assertEqual(
            possibles,
            [(4, 5)]
        )

    def test_move_horizontal_left_ally(self):
        board = Board(for_test=True)
        rook = Rook("White", board)
        board.place_piece(4, 4, rook)  
        ally_piece = Pawn("White", board)
        board.place_piece(4, 5, ally_piece) 
        possibles = rook.possible_positions_hl(4, 4)
        self.assertEqual(
            possibles,
            []
        )

    def test_move_horizontal_right_empty(self):
        board = Board(for_test=True)
        rook = Rook("White", board)
        board.place_piece(4, 4, rook)  
        possibles = rook.possible_positions_hr(4, 4)
        self.assertEqual(
            possibles,
            [(4, 3), (4, 2), (4, 1), (4, 0)]
        )

    def test_move_horizontal_right_opponent(self):
        board = Board(for_test=True)
        rook = Rook("White", board)
        board.place_piece(4, 4, rook)  
        opponent_piece = Pawn("Black", board)
        board.place_piece(4, 3, opponent_piece) 
        possibles = rook.possible_positions_hr(4, 4)
        self.assertEqual(
            possibles,
            [(4, 3)]
        )

    def test_move_horizontal_right_ally(self):
        board = Board(for_test=True)
        rook = Rook("White", board)
        board.place_piece(4, 4, rook)  
        ally_piece = Pawn("White", board)
        board.place_piece(4, 3, ally_piece) 
        possibles = rook.possible_positions_hr(4, 4)
        self.assertEqual(
            possibles,
            []
        )
if __name__ == "__main__":
    unittest.main()
