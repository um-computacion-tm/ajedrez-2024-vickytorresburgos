import unittest
from game.board import Board
from game.rook import Rook

class TestRookMovements(unittest.TestCase):
    def setUp(self):
        self.board = Board(for_test=True)  
        self.white_rook = Rook("White", self.board,5) 
        self.black_rook = Rook("Black", self.board,5) 
        
    def test_white_str(self):
        self.assertEqual(self.white_rook.white_str(), "♖")

    def test_black_str(self):
        self.assertEqual(self.black_rook.black_str(), "♜")

    def test_possible_positions_white_rook(self):
        self.board.place_piece(4, 4, self.white_rook)
        possibles = self.white_rook.possible_positions(4, 4, [(-1, 0), (1, 0), (0, -1), (0, 1)], True)
        expected = [
            (3, 4), (2, 4), (1, 4), (0, 4),
            (5, 4), (6, 4), (7, 4),
            (4, 3), (4, 2), (4, 1), (4, 0),
            (4, 5), (4, 6), (4, 7)
        ]
        self.assertEqual(possibles, expected)

            # Test for a white rook at the edge of the board
    def test_white_rook_board_edge(self):
        self.board.place_piece(0, 0, self.white_rook)
        possibles = self.white_rook.possible_positions(0, 0, [(-1, 0), (1, 0), (0, -1), (0, 1)], True)
        expected = [
            (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),
            (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7)
        ]
        self.assertEqual(possibles, expected)

    def test_possible_positions_black_rook(self):
        self.board.place_piece(4, 4, self.black_rook)
        possibles = self.black_rook.possible_positions(4, 4, [(-1, 0), (1, 0), (0, -1), (0, 1)], True)
        expected = [
            (3, 4), (2, 4), (1, 4), (0, 4),
            (5, 4), (6, 4), (7, 4),
            (4, 3), (4, 2), (4, 1), (4, 0),
            (4, 5), (4, 6), (4, 7)
        ]
        self.assertEqual(possibles, expected)

    def test_black_rook_board_edge(self):
        self.board.place_piece(0, 0, self.black_rook)
        possibles = self.black_rook.possible_positions(0, 0, [(-1, 0), (1, 0), (0, -1), (0, 1)], True)
        expected = [
            (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),
            (0, 1), (0, 2)]
        
if __name__ == '__main__':
    unittest.main()
