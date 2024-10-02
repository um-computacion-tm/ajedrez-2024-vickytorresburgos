import unittest
from game.board import Board
from game.chess import Chess
from game.exceptions import EmptyPosition, InvalidDestination, InvalidTurn, OutOfBoard
from game.pawn import Pawn
from game.player import Player

class TestChess(unittest.TestCase):
    def setUp(self):
        self.chess = Chess()  

    def test_initialization(self):
        self.assertIsInstance(self.chess.__board__, Board) 
        self.assertEqual(len(self.chess.players), 2)
        self.assertIsInstance(self.chess.players[0], Player)
        self.assertIsInstance(self.chess.players[1], Player)
        self.assertEqual(self.chess.players[0].color, "White")
        self.assertEqual(self.chess.players[1].color, "Black")
        self.assertEqual(self.chess.actual_player, self.chess.players[0])

    def test_is_playing(self):
        self.assertTrue(self.chess.is_playing())

    def test_validate_move_out_of_board(self):
        with self.assertRaises(OutOfBoard):
            self.chess.validate_move(0, 0, 8, 0)
        with self.assertRaises(OutOfBoard):
            self.chess.validate_move(0, 0, 0, 8)
        with self.assertRaises(OutOfBoard):
            self.chess.validate_move(0, 0, -1, 0)
        with self.assertRaises(OutOfBoard):
            self.chess.validate_move(0, 0, 0, -1)

    def test_validate_move_empty_position(self):
        with self.assertRaises(EmptyPosition):
            self.chess.validate_move(4, 4, 5, 5)

    def test_validate_move_invalid_turn(self):
        with self.assertRaises(InvalidTurn):
            self.chess.validate_move(1, 1, 2, 2)

    def test_validate_move_invalid_destination(self):
        with self.assertRaises(InvalidDestination):
            self.chess.validate_move(6, 0, 7, 1)

    def test_get_player_white(self):
        white_player = self.chess.get_player(0)
        self.assertEqual(white_player.color, "White")

    def test_get_player_black(self):
        black_player = self.chess.get_player(1)
        self.assertEqual(black_player.color, "Black")

    def test_move(self):
        self.assertEqual(self.chess.actual_player.color, "Black")
        self.chess.move(0, 0, 5, 0)

    def test_show_board_initial_state(self):
        expected_board_str = (
            "♜ ♞ ♝ ♛ ♚ ♝ ♞ ♜ \n"
            "♟ ♟ ♟ ♟ ♟ ♟ ♟ ♟ \n"
            "                \n"
            "                \n"
            "                \n"
            "                \n"
            "♙ ♙ ♙ ♙ ♙ ♙ ♙ ♙ \n"
            "♖ ♘ ♗ ♕ ♔ ♗ ♘ ♖ \n"
        )
        self.assertEqual(self.chess.show_board, expected_board_str)

    def test_change_turn(self):
        self.chess.change_turn()
        self.assertEqual(self.chess.actual_player.color, "Black")
        self.chess.change_turn()
        self.assertEqual(self.chess.actual_player.color, "White") 

    def test_change_turn_white_to_black(self):
        self.assertEqual(self.chess.actual_player.color, "White")
        self.chess.change_turn()
        self.assertEqual(self.chess.actual_player.color, "Black")
    
    def test_change_turn_black_to_white(self):
        self.chess.change_turn()
        self.assertEqual(self.chess.actual_player.color, "Black")
        self.chess.change_turn()
        self.assertEqual(self.chess.actual_player.color, "White") 


if __name__ == "__main__":
    unittest.main()
