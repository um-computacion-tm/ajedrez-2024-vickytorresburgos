import unittest
from game.board import Board
from game.chess import Chess, EmptyPosition, InvalidDestination, InvalidTurn, OutOfBoard
from game.pawn import Pawn
from game.player import Player
from game.rook import Rook

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
            self.chess.validate_move(6, 0, 6, 1)

    def test_move(self):
        self.chess.move(6, 0, 5, 0)
        self.assertEqual(self.chess.actual_player.color, "White")

    def test_change_turn(self):
        self.chess.change_turn()
        self.assertEqual(self.chess.actual_player.color, "Black")
        self.chess.change_turn()
        self.assertEqual(self.chess.actual_player.color, "White")        

if __name__ == "__main__":
    unittest.main()
