import unittest
from unittest.mock import patch, MagicMock
from game.board import Board
from game.pawn import Pawn
from game.piece import Piece

class TestPawn(unittest.TestCase):
    def setUp(self):
        self.board = Board()
        self.white_pawn = Pawn(color='White', board=self.board, score=1)
        self.black_pawn = Pawn(color='Black', board=self.board, score=1)
        self.board.place_piece(1, 0, self.white_pawn)
        self.board.place_piece(6, 0, self.black_pawn)

    def test_white_str(self):
        self.assertEqual(self.white_pawn.white_str(), "♙")

    def test_black_str(self):
        self.assertEqual(self.black_pawn.black_str(), "♟")

    def test_white_pawn_possible_positions(self):
        self.board.place_piece(6, 3, self.white_pawn)
        possibles = self.white_pawn.possible_positions(6, 3)
        expected = [(5, 3), (4, 3)]
        self.assertEqual(possibles, expected)

    def test_white_pawn_middle_position(self):
        self.board.place_piece(3, 3, self.white_pawn)
        possibles = self.white_pawn.possible_positions(3, 3)
        expected = [(2, 3)]
        self.assertEqual(possibles, expected)

    def test_possible_positions_black_pawn(self):
        self.board.place_piece(1, 3, self.black_pawn)
        possibles = self.black_pawn.possible_positions(1, 3)
        expected = [(2, 3), (3, 3)]
        self.assertEqual(possibles, expected)

    def test_black_pawn_middle_position(self):
        self.board.place_piece(4, 3, self.black_pawn)
        possibles = self.black_pawn.possible_positions(4, 3)
        expected = [(5, 3)]
        self.assertEqual(possibles, expected)

    def test_possible_positions_edge_cases(self):
        self.board.place_piece(6, 0, self.white_pawn)
        possibles = self.white_pawn.possible_positions(6, 0)
        expected = [(5, 0), (4, 0)]
        self.assertEqual(possibles, expected)

    def test_black_pawn_edge(self):
        self.board.place_piece(1, 7, self.black_pawn)
        possibles = self.black_pawn.possible_positions(1, 7)
        expected = [(2, 7), (3, 7)]
        self.assertEqual(possibles, expected)

    def test_possible_positions_diagonal_captures(self):
        self.board.place_piece(3, 3, self.white_pawn)
        black_piece = Piece(color="Black", board=self.board,score=1)
        self.board.place_piece(2, 2, black_piece)
        possibles = self.white_pawn.possible_positions(3, 3)
        expected = [(2, 3), (2, 2)]
        self.assertEqual(possibles, expected)

    def test_black_pawn_capture_white_pawn_diagonal(self):
        self.board.place_piece(4, 4, self.black_pawn)
        white_piece = Piece("White",self.board, 1)
        self.board.place_piece(5, 5, white_piece)
        possibles = self.black_pawn.possible_positions(4, 4)
        expected = [(5, 4), (5, 5)]
        self.assertEqual(possibles, expected)

    def test_white_pawn_no_diagonal_captures(self):
        self.board.place_piece(3, 3, self.white_pawn)
        self.board.place_piece(2, 2, None)
        possibles = self.white_pawn.possible_positions(3, 3)
        expected = [(2, 3)]
        self.assertEqual(possibles, expected)

    def test_black_pawn_no_diagonal_captures(self):
        self.board.place_piece(4, 4, self.black_pawn)
        self.board.place_piece(5, 5, None)
        possibles = self.black_pawn.possible_positions(4, 4)
        expected = [(5, 4)]
        self.assertEqual(possibles, expected)

    @patch.object(Pawn, 'get_color', return_value='White')
    @patch.object(Board, 'get_piece', return_value=Piece("Black", None, 1))
    
    def test_possible_positions_diagonal_capture_white_pawn(self, mock_get_piece, mock_get_color):
        self.board.place_piece(3, 3, self.white_pawn)
        possibles = self.white_pawn.possible_positions(3, 3)
        expected = [(2, 3), (2, 2), (2, 4)]
        self.assertEqual(possibles, expected)

    @patch.object(Pawn, 'get_color', return_value='Black')
    @patch.object(Board, 'get_piece', return_value=Piece("White", None, 1))
    def test_possible_positions_diagonal_capture_black_pawn(self, mock_get_piece, mock_get_color):
        self.board.place_piece(4, 4, self.black_pawn)
        possibles = self.black_pawn.possible_positions(4, 4)
        expected = [(5, 4), (5, 3), (5, 5)]
        self.assertEqual(possibles, expected)

if __name__ == '__main__':
    unittest.main()
