import unittest
from unittest.mock import patch
from game.chess import Chess
from game.cli import play
from game.exceptions import EmptyPosition, InvalidDestination, InvalidMove, InvalidTurn, OutOfBoard, PathBlocked

class TestCli(unittest.TestCase):
    
    @patch('builtins.input', side_effect=['1', '1', '3', '1']) 
    @patch.object(Chess,'move') 
    def test_play(self, mock_move, mock_input):
        chess = Chess()
        play(chess)  
        mock_move.assert_called_once_with(0, 0, 2, 0)

    @patch('builtins.input', side_effect=['7', 'a', '7', '1', '6', '1'])
    @patch.object(Chess,'move', side_effect = ValueError("Unexpected input. Please try again"))
    @patch('builtins.print') 
    def test_play_invalid_input(self, mock_print, mock_move, mock_input):
        chess = Chess()
        play(chess)
        mock_print.assert_any_call("Unexpected input. Please try again")
        play(chess)
        mock_move.assert_called_once_with(6, 0, 5, 0)

    @patch('builtins.input', side_effect=['1', '1', '9', '1', '7', '1', '6', '1'])
    @patch.object(Chess,'move', side_effect = OutOfBoard("The position selected is out of the board"))
    @patch('builtins.print') 
    def test_play_out_of_board(self, mock_print, mock_move, mock_input):
        chess = Chess()
        play(chess)
        mock_move.assert_called_once_with(0, 0, 8, 0)
        mock_print.assert_any_call("The position selected is out of the board")
        mock_print.assert_any_call("Try again.")
    
    @patch('builtins.input', side_effect=['5', '4', '5', '1', '7', '1', '6', '1'])
    @patch.object(Chess, 'move', side_effect = EmptyPosition("The position is empty"))
    @patch('builtins.print') 
    def test_play_empty_position(self, mock_print, mock_move, mock_input):
        chess = Chess()
        play(chess)
        mock_move.assert_called_once_with(4, 3, 4, 0)
        mock_print.assert_any_call("The position is empty")
        mock_print.assert_any_call("Try again.")

    @patch('builtins.input', side_effect=['1', '1', '3', '1', '1', '1', '1', '1'])
    @patch.object(Chess, 'move', side_effect = InvalidDestination("The destination selected contains a piece of your own. Try again"))
    @patch('builtins.print')
    def test_play_invalid_destination(self, mock_print, mock_move, mock_input):
        chess = Chess()
        play(chess)
        mock_move.assert_called_once_with(0, 0, 2, 0)
        mock_print.assert_any_call("The destination selected contains a piece of your own. Try again")
        mock_print.assert_any_call("Try again.")

    @patch('builtins.input', side_effect=['1', '1', '3', '1', '1', '1', '1', '1'])
    @patch.object(Chess, 'move', side_effect = InvalidTurn("Invalid Turn. You cannot move your opponent's pieces"))
    @patch('builtins.print')
    def test_play_invalid_turn(self, mock_print, mock_move, mock_input):
        chess = Chess()
        play(chess)
        mock_move.assert_called_once_with(0, 0, 2, 0)
        mock_print.assert_any_call("Invalid Turn. You cannot move your opponent's pieces")
        mock_print.assert_any_call("Try again.")

    @patch('builtins.input', side_effect=['1', '1', '3', '1', '1', '1', '1', '1'])
    @patch.object(Chess, 'move', side_effect = InvalidMove("The move is not valid"))
    @patch('builtins.print')
    def test_play_invalid_move(self, mock_print, mock_move, mock_input):
        chess = Chess()
        play(chess)
        mock_move.assert_called_once_with(0, 0, 2, 0)
        mock_print.assert_any_call("The move is not valid")
        mock_print.assert_any_call("Try again.")


    @patch('builtins.input', side_effect=['1', '1', '3', '1', '1', '1', '1', '1'])
    @patch.object(Chess, 'move', side_effect = PathBlocked("There is a piece blocking the path"))
    @patch('builtins.print')
    def test_play_path_blocked(self, mock_print, mock_move, mock_input):
        chess = Chess()
        play(chess)
        mock_move.assert_called_once_with(0, 0, 2, 0)
        mock_print.assert_any_call("There is a piece blocking the path")
        mock_print.assert_any_call("Try again.")

if __name__ == '__main__':
    unittest.main()
    