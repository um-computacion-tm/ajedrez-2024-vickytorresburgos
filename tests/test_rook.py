import unittest

from game.board import Board, InvalidCoordException
from game.piece import Piece
from game.rook import Rook

class TestRookMovements(unittest.TestCase):
    def setUp(self):
        self.board = Board()
        self.rook = Rook("White", self.board)

    def test_possible_positions_empty_board(self):
        self.board.place_piece(4, 4, self.rook)
        expected_positions = [
            (0, 4), (1, 4), (2, 4), (3, 4), (5, 4), (6, 4), (7, 4),
            (4, 0), (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (4, 7)
        ]
        self.assertEqual(self.rook.possible_positions(4, 4), expected_positions)

    def test_possible_positions_with_obstacles(self):
        self.board.place_piece(4, 4, self.rook)
        self.board.place_piece(4, 6, Piece("Black", self.board))  # Obstacle
        self.board.place_piece(6, 4, Piece("White", self.board))  # Friendly piece
        expected_positions = [
            (0, 4), (1, 4), (2, 4), (3, 4), (5, 4),
            (4, 0), (4, 1), (4, 2), (4, 3), (4, 5), (4, 6)
        ]
        self.assertEqual(self.rook.possible_positions(4, 4), expected_positions)

    def test_possible_positions_invalid_coordinates(self):
        with self.assertRaises(InvalidCoordException):
            self.rook.possible_positions(8, 4)

        with self.assertRaises(InvalidCoordException):
            self.rook.possible_positions(4, 8)

        with self.assertRaises(InvalidCoordException):
            self.rook.possible_positions(-1, 4)

        with self.assertRaises(InvalidCoordException):
            self.rook.possible_positions(4, -1)

if __name__ == '__main__':
    unittest.main()
