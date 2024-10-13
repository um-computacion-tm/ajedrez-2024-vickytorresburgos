from game.piece import Piece

class Knight(Piece):

    def __init__(self, color, board, score):
        super().__init__(color, board, score)
        self.__directions__ = [(-2, 1), (-2, -1), (2, 1), (2, -1), (1, 2), (-1, 2), (1, -2), (-1, -2)]
    
    def white_str(self):
        # """
        # Returns the Unicode character for a white knight.

        # Returns:
        #     str: The Unicode character for a white knight.
        # """
        return "♘"

    def black_str(self):
        # """
        # Returns the Unicode character for a black knight.

        # Returns:
        #     str: The Unicode character for a black knight.
        # """
        return "♞"

