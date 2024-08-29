import unittest
from game.board import Board
from game.rook import Rook
from game.pawn import Pawn

class TestRook(unittest.TestCase):

    def test_str_white(self):
        rook = Rook('White', self)
        self.assertEqual(rook.white_str(), '♖')

    def test_black_str(self):
        rook = Rook('Black', self)
        self.assertEqual(rook.black_str(), '♜')

    # def test_move_vertical_desc(self):
    #     board = Board()
    #     rook = Rook("White", board)
    #     possibles = rook.possible_positions_vd(4,1)
    #     self.assertEqual(possibles,[(5,1),(6,1),(7,1)])

    def test_move_vertical_asc(self):
        board = Board()
        rook = Rook("White", board)
        possibles = rook.possible_positions_va(4, 1)
        self.assertEqual(possibles,[(3, 1), (2, 1), (1, 1), (0, 1)])

    def test_move_vertical_desc_with_own_piece(self):
        board = Board()
        board.place_piece(6, 1, Pawn("White", board))
        rook = Rook("White", board)
        board.place_piece(4, 1, rook)
        possibles = rook.possible_positions_vd(4, 1)
        self.assertEqual(possibles,[(5, 1)])

    def test_move_vertical_desc_with_not_own_piece(self):
        board = Board()
        board.place_piece(6, 1, Pawn("BLACK", board))
        rook = Rook("White", board)
        board.place_piece(4, 1, rook)
        possibles = rook.possible_positions_vd(4, 1)
        self.assertEqual(possibles,[(5, 1), (6, 1)])

if __name__ == "__main__":
    unittest.main()
