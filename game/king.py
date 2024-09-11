from game.piece import Piece

class King(Piece):
    def white_str(self):
        return "♔"

    def black_str(self):
        return "♚"