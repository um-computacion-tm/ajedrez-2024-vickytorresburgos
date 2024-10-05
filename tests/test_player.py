import unittest
from game.player import Player

class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player_white = Player("White")
        self.player_black = Player("Black")

    def test_initialization(self):
        self.assertEqual(self.player_white.color, "White")
        self.assertEqual(self.player_white.pieces, 16)
        self.assertEqual(self.player_white.score, 0)

        self.assertEqual(self.player_black.color, "Black")
        self.assertEqual(self.player_black.pieces, 16)
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
        self.assertEqual(self.player_white.pieces, 15)

        self.player_black.remove_piece()
        self.assertEqual(self.player_black.pieces, 15)

    def test_remove_piece_multiple(self):
        self.player_white.remove_piece()
        self.player_white.remove_piece()
        self.assertEqual(self.player_white.pieces, 14)

        self.player_black.remove_piece()
        self.player_black.remove_piece()
        self.player_black.remove_piece()
        self.assertEqual(self.player_black.pieces, 13)

    def test_remove_piece_all(self):
        for _ in range(16):
            self.player_white.remove_piece()
        self.assertEqual(self.player_white.pieces, 0)

        for _ in range(16):
            self.player_black.remove_piece()
        self.assertEqual(self.player_black.pieces, 0)

    def test_remove_piece_beyond_zero(self):
        for _ in range(17):
            self.player_white.remove_piece()
        self.assertEqual(self.player_white.pieces, -1)

        for _ in range(17):
            self.player_black.remove_piece()
        self.assertEqual(self.player_black.pieces, -1)
        
if __name__ == "__main__":
    unittest.main()
