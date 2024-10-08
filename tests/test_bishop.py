import unittest
from game.board import Board
from game.bishop import Bishop
from game.pawn import Pawn


class TestBishopMovements(unittest.TestCase):
    def test_move_diagonal_empty(self):
        board = Board(for_test=True)
        bishop = Bishop("White", board,3)
        board.place_piece(4, 4, bishop)  
        possibles = bishop.possible_positions(4, 4)
        self.assertEqual(
            possibles,
            [(3, 5), (2, 6), (1, 7), (3, 3), (2, 2), (1, 1), (0, 0), (5, 5), (6, 6), (7, 7), (5, 3), (6, 2), (7, 1)]
        )

    def test_move_diagonal_opponent(self):
        board = Board(for_test=True)
        bishop = Bishop("White", board,3)
        board.place_piece(4, 4, bishop)  
        opponent_piece = Pawn("Black", board,1)
        board.place_piece(3, 5, opponent_piece)  
        possibles = bishop.possible_positions(4, 4)
        self.assertEqual(
            possibles,
            [(3, 5), (3, 3), (2, 2), (1, 1), (0, 0), (5, 5), (6, 6), (7, 7), (5, 3), (6, 2), (7, 1)]
        )

    def test_move_diagonal_ally(self):
        board = Board(for_test=True)
        bishop = Bishop("White", board,3)
        board.place_piece(4, 4, bishop) 
        ally_piece = Pawn("White", board,1)
        board.place_piece(3, 5, ally_piece) 
        possibles = bishop.possible_positions(4, 4)
        self.assertEqual(
            possibles,
            [(3, 3), (2, 2), (1, 1), (0, 0), (5, 5), (6, 6), (7, 7), (5, 3), (6, 2), (7, 1)]
        )

if __name__ == '__main__':
    unittest.main()
