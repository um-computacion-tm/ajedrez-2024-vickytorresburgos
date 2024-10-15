import unittest
from game.player import Player

class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player_white = Player("White",16)
        self.player_black = Player("Black",16)

    def test_initialization(self):
        self.assertEqual(self.player_white.color, "White")
        self.assertEqual(self.player_white.piece, 16)
        self.assertEqual(self.player_white.score, 0)

        self.assertEqual(self.player_black.color, "Black")
        self.assertEqual(self.player_black.piece, 16)
        self.assertEqual(self.player_black.score, 0)

    def test_sum_score_positive(self):
        self.player_white.sum_score(5)
        self.assertEqual(self.player_white.score, 5)

        self.player_white.sum_score(3)
        self.assertEqual(self.player_white.score, 8)

        self.player_black.sum_score(10)
        self.assertEqual(self.player_black.score, 10)

    def test_sum_score_zero(self):
        self.player_white.sum_score(0)
        self.assertEqual(self.player_white.score, 0)

    def test_sum_score_negative(self):
        self.player_white.sum_score(-5)
        self.assertEqual(self.player_white.score, -5)

        self.player_white.sum_score(10)
        self.assertEqual(self.player_white.score, 5)

    def test_remove_piece_single(self):
        self.player_white.remove_piece()
        self.assertEqual(self.player_white.piece, 15)

        self.player_black.remove_piece()
        self.assertEqual(self.player_black.piece, 15)

    def test_remove_piece_multiple(self):
        self.player_white.remove_piece()
        self.player_white.remove_piece()
        self.assertEqual(self.player_white.piece, 14)

        self.player_black.remove_piece()
        self.player_black.remove_piece()
        self.player_black.remove_piece()
        self.assertEqual(self.player_black.piece, 13)

    def test_remove_piece_all(self):
        for _ in range(16):
            self.player_white.remove_piece()
        self.assertEqual(self.player_white.piece, 0)

        for _ in range(16):
            self.player_black.remove_piece()
        self.assertEqual(self.player_black.piece, 0)

    def test_remove_piece_beyond_zero(self):
        for _ in range(17):
            self.player_white.remove_piece()
        self.assertEqual(self.player_white.piece, -1)

        for _ in range(17):
            self.player_black.remove_piece()
        self.assertEqual(self.player_black.piece, -1)
        
if __name__ == "__main__":
    unittest.main()
