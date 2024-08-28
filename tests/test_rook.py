import unittest
from game.board import Board
from game.rook import Rook

class TestRook(unittest.TestCase):

    # def test_str(self):
    #     rook = Rook("White")
    #     self.assertEqual(str(rook),"♜")

    def test_move_vertical_desc(self):
        rook = Rook("White")
        possibles = rook.possible_positions_vd(4,0)
        self.assertEqual(possibles,[(5,0),(6,0),(7,0)])

    def test_move_vertical_asc(self):
        rook = Rook("White")
        possibles = rook.possible_positions_va(4,0)
        self.assertEqual(possibles,[(3,0),(2,0),(1,0),(0,0)])

if __name__ == "__main__":
    unittest.main()
