from game.piece import Piece

class Queen(Piece):
    def white_str(self):
        # """
        # Returns the Unicode character for a white queen.

        # Returns:
        #     str: The Unicode character for a white queen.
        # """
        return "♕"

    def black_str(self):
        # """
        # Returns the Unicode character for a black queen.

        # Returns:
        #     str: The Unicode character for a black queen.
        # """
        return "♛"

    def get_directions(self):
        return [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, 1), (-1, -1), (1, 1), (1, -1)]