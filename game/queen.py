from game.piece import Piece

class Queen(Piece):

    def __init__(self, color, board, score):
        super().__init__(color, board, score)
        self.__directions__ = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, 1), (-1, -1), (1, 1), (1, -1)]


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

