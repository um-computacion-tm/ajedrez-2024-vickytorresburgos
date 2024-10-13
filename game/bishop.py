from game.piece import Piece

class Bishop(Piece):

    def __init__(self, color, board, score):
        super().__init__(color, board, score)
        self.__directions__ = [(-1, 1), (-1, -1), (1, 1), (1, -1)]


    def white_str(self):
        """
        Returns the Unicode character for a white bishop.

        Returns:
            str: The Unicode character for a white bishop.
        """
        return "♗"

    def black_str(self):
        """
        Returns the Unicode character for a black bishop.

        Returns:
            str: The Unicode character for a black bishop.
        """

        return "♝"
    
