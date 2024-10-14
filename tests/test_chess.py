import unittest
from unittest.mock import patch, MagicMock
from game.bishop import Bishop
from game.king import King
from game.knight import Knight
from game.piece import Piece
from game.pawn import Pawn
from game.queen import Queen
from game.rook import Rook
from game.board import Board
from game.chess import Chess
from game.exceptions import EmptyPosition, InvalidDestination, InvalidMove, InvalidPawnMovement, InvalidTurn, OutOfBoard, PathBlocked
from game.player import Player

class TestChess(unittest.TestCase):
    def setUp(self):
        self.chess = Chess()
        self.board = Board()
        self.king = King("White", self.board, 1 )
        self.queen = Queen("White", self.board, 9)
        self.knight = Knight("White", self.board, 3)
        self.bishop = Bishop("White", self.board, 3)

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

    def test_show_board_initial_state(self):
        expected_board_str = ( 
            "    1   2   3   4   5   6   7   8\n"
            "  ┌───┬───┬───┬───┬───┬───┬───┬───┐\n"
            "1 │ ♜ │ ♞ │ ♝ │ ♛ │ ♚ │ ♝ │ ♞ │ ♜ │ \n" 
            "  ├───┼───┼───┼───┼───┼───┼───┼───┤\n"
            "2 │ ♟ │ ♟ │ ♟ │ ♟ │ ♟ │ ♟ │ ♟ │ ♟ │ \n" 
            "  ├───┼───┼───┼───┼───┼───┼───┼───┤\n"
            "3 │   │   │   │   │   │   │   │   │ \n"
            "  ├───┼───┼───┼───┼───┼───┼───┼───┤\n"
            "4 │   │   │   │   │   │   │   │   │ \n" 
            "  ├───┼───┼───┼───┼───┼───┼───┼───┤\n"
            "5 │   │   │   │   │   │   │   │   │ \n"
            "  ├───┼───┼───┼───┼───┼───┼───┼───┤\n"
            "6 │   │   │   │   │   │   │   │   │ \n"
            "  ├───┼───┼───┼───┼───┼───┼───┼───┤\n"
            "7 │ ♙ │ ♙ │ ♙ │ ♙ │ ♙ │ ♙ │ ♙ │ ♙ │ \n" 
            "  ├───┼───┼───┼───┼───┼───┼───┼───┤\n"
            "8 │ ♖ │ ♘ │ ♗ │ ♕ │ ♔ │ ♗ │ ♘ │ ♖ │ \n" 
            "  └───┴───┴───┴───┴───┴───┴───┴───┘"
        )
        self.assertEqual(self.chess.show_board(), expected_board_str)

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

    @patch.object(Board, 'get_piece', return_value=None)
    def test_validate_move_empty_position(self, mock_get_piece):
        with self.assertRaises(EmptyPosition):
            self.chess.validate_move(0, 0, 1, 1)

    @patch.object(Board, 'get_piece', return_value=Piece("Black", None, 1))
    def test_validate_move_invalid_turn(self, mock_get_piece):
        with self.assertRaises(InvalidTurn):
            self.chess.validate_move(0, 0, 1, 1)

    @patch.object(Board, 'get_piece', side_effect=[Piece("White", None, 1), Piece("White", None, 1)])
    def test_validate_move_invalid_destination(self, mock_get_piece):
        with self.assertRaises(InvalidDestination):
            self.chess.validate_move(0, 0, 1, 1)

    @patch.object(Pawn, 'possible_positions', return_value=[])
    @patch.object(Board, 'get_piece', return_value=Piece("White", None, 1))
    def test_validate_move_invalid_move(self, mock_get_piece, mock_possible_positions):
        with self.assertRaises(InvalidMove):
            self.chess.validate_move(0, 0, 1, 1)

    @patch.object(Pawn, 'possible_positions', return_value=[(1, 1)])
    @patch.object(Board, 'get_piece', side_effect=[Pawn("White", None, 1), None])
    def test_validate_move_invalid_pawn_movement(self, mock_get_piece, mock_possible_positions):
        with self.assertRaises(InvalidPawnMovement):
            self.chess.validate_move(0, 0, 1, 1)

    def test_rook_invalid_move(self):
        chess = Chess()
        board = Board(for_test=True)
        self.chess.__board__.place_piece(1,1,Rook('White', board, 5))
        self.chess.__board__.get_piece(1,1)
        with self.assertRaises(InvalidMove):
            self.chess.validate_move(1,1,2,2)

    def test_path_blocked(self):
        chess = Chess()
        board = Board(for_test = False)
        self.chess.__board__.get_piece(7,0)
        with self.assertRaises(PathBlocked):
            self.chess.validate_move(7,0,5,0)

    def test_valid_move(self):
        chess = Chess()
        board = Board(for_test = False)
        chess.move(6, 0, 4, 0)
        piece = chess.__board__.get_piece(4,0)
        self.assertIsInstance(piece,Pawn)

    @patch.object(Chess, 'validate_move', return_value=[])
    def test_sum_score(self, mock_validate_move):
        chess = Chess()
        board = Board(for_test = True)
        self.chess.__board__.place_piece(0,0,Pawn('White', board, 1))
        self.chess.__board__.place_piece(1,1,Pawn('Black', board, 1))
        self.chess.move(0, 0, 1, 1)
        self.assertEqual(self.chess.get_player(0).score, 1)
        self.assertEqual(self.chess.get_player(1).pieces, 15)

    @patch.object(Chess, 'validate_move', return_value = [])
    def test_remove_piece(self, mock_validate_move):
        chess = Chess()
        board = Board(for_test = True)
        self.chess.__board__.place_piece(0,0,Pawn('Black', board, 1))
        self.chess.__board__.place_piece(1,1,Pawn('White', board, 1))
        self.chess.change_turn()
        self.chess.move(0, 0, 1, 1)
        self.assertEqual(self.chess.get_player(1).score, 1)
        self.assertEqual(self.chess.get_player(0).pieces, 15)

    def test_king_movement(self):
        expected_positions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, 1), (-1, -1), (1, 1), (1, -1)]
        positions, more_than_one_step = self.chess.movement(self.king)
        self.assertEqual(positions, expected_positions)
        self.assertEqual(more_than_one_step, False)

    def test_queen_movement(self):
        expected_positions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, 1), (-1, -1), (1, 1), (1, -1)]
        positions, more_than_one_step = self.chess.movement(self.queen)
        self.assertEqual(positions, expected_positions)
        self.assertEqual(more_than_one_step, True)  

    def test_knight_movement(self):
        expected_positions = [(-2, 1), (-2, -1), (2, 1), (2, -1), (1, 2), (-1, 2), (1, -2), (-1, -2)]
        positions, more_than_one_step = self.chess.movement(self.knight)
        self.assertEqual(positions, expected_positions)
        self.assertEqual(more_than_one_step, False)  

    def test_bishop_movement(self):
        expected_positions = [(-1, 1), (-1, -1), (1, 1), (1, -1)]
        positions, more_than_one_step = self.chess.movement(self.bishop)
        self.assertEqual(positions, expected_positions)
        self.assertEqual(more_than_one_step, True)  

if __name__ == "__main__":
    unittest.main()
