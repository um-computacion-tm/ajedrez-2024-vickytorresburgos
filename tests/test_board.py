import unittest
from game.board import Board
from game.rook import Rook

class TestBoard(unittest.TestCase):

    def setUp(self):
        self.board = Board()

    def test_posicion_inicial(self): #testea posicion inicial de la torre
       
        self.assertIsInstance(self.board.get_piece(0, 0), Rook) #
        self.assertEqual(self.board.get_piece(0, 0).color, "Black")

        self.assertIsInstance(self.board.get_piece(0, 7), Rook)
        self.assertEqual(self.board.get_piece(0, 7).color, "Black")

        self.assertIsInstance(self.board.get_piece(7, 0), Rook)
        self.assertEqual(self.board.get_piece(7, 0).color, "White")

        self.assertIsInstance(self.board.get_piece(7, 7), Rook)
        self.assertEqual(self.board.get_piece(7, 7).color, "White")

# Usa assertIsInstance para verificar 
# que en las posiciones (0, 0), (0, 7), (7, 0), y (7, 7) hay una instancia de Rook.
# Usa assertEqual para verificar que la pieza en esas posiciones es negra o blanca

    def test_empty_positions(self):

        self.assertIsNone(self.board.get_piece(1, 1))
        self.assertIsNone(self.board.get_piece(6, 6))
        self.assertIsNone(self.board.get_piece(4, 4))

# Verifica que las posiciones del tablero que deberían estar vacías contengan None.

if __name__ == "__main__":
    unittest.main()
