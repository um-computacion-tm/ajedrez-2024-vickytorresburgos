import unittest
from unittest.mock import patch
from game.chess import Chess
from game.cli import play, validate_input, RangeError
    
class TestCli(unittest.TestCase):
    @patch('builtins.input',side_effect=['1', '1', '2', '2'])
    @patch('builtins.print')
    @patch.object(Chess, 'move')
    @patch('game.cli.validate_input')

    def test_happy_path(self,mock_validate_input,mock_chess_move,mock_print,mock_input):
        chess = Chess()
        play(chess)
        self.assertEqual(mock_validate_input.call_count, 4)
        self.assertEqual(mock_chess_move.call_count, 1)
        self.assertEqual(mock_print.call_count, 1)
        self.assertEqual(mock_input.call_count, 4)


    @patch('builtins.input',side_effect=['hola', '1', '2', '2'])
    @patch('builtins.print') 
    @patch.object(Chess, 'move')
    @patch('game.cli.validate_input')

    def test_not_happy_path(self,mock_validate_input,mock_chess_move,mock_print,mock_input):
        chess = Chess()
        play(chess)
        self.assertEqual(mock_validate_input.call_count, 0)
        self.assertEqual(mock_chess_move.call_count, 0)
        self.assertEqual(mock_print.call_count, 2)
        self.assertEqual(mock_input.call_count, 1)


    @patch('builtins.input',side_effect=['1', '1', '2', 'hola'])
    @patch('builtins.print') 
    @patch.object(Chess, 'move')
    @patch('game.cli.validate_input')


    def test_more_not_happy_path(self,mock_validate_input,mock_chess_move,mock_print,mock_input):
        chess = Chess()
        play(chess)
        self.assertEqual(mock_input.call_count, 4)
        self.assertEqual(mock_print.call_count, 2)
        self.assertEqual(mock_chess_move.call_count, 0)
        self.assertEqual(mock_validate_input.call_count, 3)
    

    @patch('builtins.input',side_effect=['10', '1', '2', '1'])
    @patch('builtins.print') 
    @patch.object(Chess, 'move')
    @patch('game.cli.validate_input', side_effect = [RangeError])

    def test_range_error(self,mock_validate_input,mock_chess_move,mock_print,mock_input):
        chess = Chess()
        play(chess)
        self.assertEqual(mock_input.call_count, 1)
        self.assertEqual(mock_print.call_count, 2)
        self.assertEqual(mock_chess_move.call_count, 0)
        self.assertEqual(mock_validate_input.call_count, 1)
  

    def test_valid_input(self):
        chess = Chess()
        self.assertEqual(validate_input(1), None)
        self.assertEqual(validate_input(5), None)
        self.assertEqual(validate_input(8), None)

    def test_invalid_range_input(self):
        chess = Chess()
        with self.assertRaises(RangeError):
            validate_input(10)
        with self.assertRaises(RangeError):
            validate_input(-1)


if __name__ == '__main__':
    unittest.main()