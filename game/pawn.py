from game.piece import Piece

class Pawn(Piece):
    def white_str(self):
        return "♙"

    def black_str(self):
        return "♟"