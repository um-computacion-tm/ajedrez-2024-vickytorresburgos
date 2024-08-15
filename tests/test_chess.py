import unittest
from game.chess import Chess

class TestChess(unittest.TestCase):
    
    def setUp(self):
        self.chess = Chess()

    def test_move_changes_turn(self):
        self.chess.move(1, 0, 2, 0)  # Asumiendo un movimiento válido
        self.assertEqual(self.chess.turn, "Black")
        self.chess.move(6, 0, 5, 0)  # Asumiendo otro movimiento válido
        self.assertEqual(self.chess.turn, "White")

    def test_turno_inicial(self): #verifica que el turno inicial sea del "White"
        self.assertEqual(self.chess.turn, "White") 

    def test_change_turn(self): #verifica el cambio de turno
        self.chess.change_turn()
        self.assertEqual(self.chess.turn, "Black")
        self.chess.change_turn()
        self.assertEqual(self.chess.turn, "White")

if __name__ == "__main__":
    unittest.main()
