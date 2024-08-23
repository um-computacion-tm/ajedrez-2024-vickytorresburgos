import unittest
from unittest.mock import patch
from game.chess import Chess
from game.cli import play, validate_input
    
class TestCli(unittest.TestCase):

    @patch('builtins.input', side_effect = ['1','1','2','2'])
    @patch('builtins.print')
    @patch.object(Chess, 'move')

    def test_happy_path(self,mock_chess_move,mock_print,mock_input):
        chess = Chess()
        play(chess)
        self.assertEqual(mock_input.call_count,4)
        self.assertEqual(mock_print.call_count,1)
        self.assertEqual(mock_chess_move.call_count,1)

    @patch('builtins.input', side_effect = ['hola','1','2','2'])
    @patch('builtins.print') # este patch controla lo que hace el print
    @patch.object(Chess, 'move')

    def test_not_happy_path(self,mock_chess_move,mock_print,mock_input): 
        chess = Chess()
        play(chess)
        self.assertEqual(mock_input.call_count, 1)
        self.assertEqual(mock_print.call_count, 2)
        self.assertEqual(mock_chess_move.call_count, 0)

    def test_valid_input(self):
        chess = Chess()
        self.assertEqual(validate_input('5'), 5)
        self.assertEqual(validate_input('0'), 0)
        self.assertEqual(validate_input('8'), 8)

    def test_invalid_range_input(self):
        chess = Chess()
        with self.assertRaises(ValueError):
            validate_input('10')
        with self.assertRaises(ValueError):
            validate_input('-1')

    def test_invalid_input_not_integer(self):
        chess = Chess()
        with self.assertRaises(ValueError):
            validate_input('hola')
        with self.assertRaises(ValueError):
            validate_input('5.5')
        with self.assertRaises(ValueError):
            validate_input(' ')
        

if __name__ == '__main__':
    unittest.main()