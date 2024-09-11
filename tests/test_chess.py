import unittest
from game.chess import Chess
class TestChess(unittest.TestCase):
    
    def setUp(self):
        self.chess = Chess()

    def test_is_playing(self):
        self.assertTrue(self.chess.is_playing())

    # def test_move_changes_turn(self):
    #     self.chess.move(2, 0, 2, 0) 
    #     self.assertEqual(self.chess.turn, "Black")
    #     self.chess.move(6, 0, 5, 0)
    #     self.assertEqual(self.chess.turn, "White")

    def test_turno_inicial(self):
        self.assertEqual(self.chess.turn, "White") 

    def test_change_turn(self):
        self.chess.change_turn()
        self.assertEqual(self.chess.turn, "Black")
        self.chess.change_turn()
        self.assertEqual(self.chess.turn, "White")

    def test_board_display(self):
        board_display = self.chess.show_board()
        self.assertIsInstance(board_display, str)

if __name__ == "__main__":
    unittest.main()
