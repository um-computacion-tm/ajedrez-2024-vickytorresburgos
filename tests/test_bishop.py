import unittest
from game.board import Board
from game.bishop import Bishop

class TestBishopMovements(unittest.TestCase):
    def setUp(self):
        self.board = Board(for_test=True)
        self.white_bishop = Bishop(color='White', board=self.board, score=3)
        self.black_bishop = Bishop(color='Black', board=self.board, score=3)
        self.board.place_piece(4, 4, self.white_bishop)
        self.board.place_piece(7, 0, self.black_bishop)

    def test_white_str(self):
        self.assertEqual(self.white_bishop.white_str(), "♗")

    def test_black_str(self):
        self.assertEqual(self.black_bishop.black_str(), "♝")

    def test_move_diagonal_white_bishop(self):
        possibles = self.white_bishop.possible_positions(4, 4, [(-1, 1), (-1, -1), (1, 1), (1, -1)], True)
        self.assertEqual(
            possibles,
            [(3, 5), (2, 6), (1, 7), (3, 3), (2, 2), (1, 1), (0, 0), (5, 5), (6, 6), (7, 7), (5, 3), (6, 2), (7, 1)]
        )

    def test_move_diagonal_black_bishop(self): 
        possibles = self.black_bishop.possible_positions(7, 0, [(-1, 1), (-1, -1), (1, 1), (1, -1)], True)
        self.assertEqual(
            possibles,
            [(6, 1), (5, 2), (4, 3), (3, 4), (2, 5), (1, 6), (0, 7)]        
            )

if __name__ == '__main__':
    unittest.main()
