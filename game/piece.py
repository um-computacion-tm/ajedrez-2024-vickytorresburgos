class Piece:
    def __init__(self, color, board, score, directions):
        """
        Initializes a new piece.

        Parameters:
            color (str): The color of the piece ("White" or "Black").
            board (Board): The chessboard the piece is on.
            score (int): The score value of the piece.
        """
        self.__color__ = color
        self.__board__ = board
        self.__score__ = score
        self.__directions__ = directions

    def white_str(self):
        """
        Returns the Unicode character for a white piece.

        Returns:
            str: The Unicode character for a white piece.
        """
        return ""

    def black_str(self):
        """
        Returns the Unicode character for a black piece.

        Returns:
            str: The Unicode character for a black piece.
        """
        return ""

    def __str__(self):
        """
        Returns the string representation of the piece based on its color.

        Returns:
            str: The string representation of the piece.
        """
        if self.__color__ == "White":
            return self.white_str()
        else:
            return self.black_str()

    def get_color(self):
        """
        Returns the color of the piece.

        Returns:
            str: The color of the piece ("White" or "Black").
        """
        return self.__color__

    def get_score(self):
        """
        Returns the score value of the piece.

        Returns:
            int: The score value of the piece.
        """
        return self.__score__
    
    def get_directions(self):
        return []

    def possible_positions(self, row, col, more_than_one_step):
        possibles = []
        directions = self.get_directions()
        for dr, dc in directions:
            next_row, next_col = row + dr, col + dc
            if more_than_one_step: 
                while 0 <= next_row < 8 and 0 <= next_col < 8:
                    possibles.append((next_row, next_col))
                    next_row += dr
                    next_col += dc
            else:
                if 0 <= next_row < 8 and 0 <= next_col < 8:
                    possibles.append((next_row, next_col))
        return possibles
    
