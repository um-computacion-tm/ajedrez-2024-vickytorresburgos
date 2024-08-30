from game.piece import Piece

class Queen(Piece):
    def white_str(self):
        return "♕"

    def black_str(self):
        return "♛"