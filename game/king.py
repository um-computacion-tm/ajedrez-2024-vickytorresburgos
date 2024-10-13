from game.piece import Piece

class King(Piece):
    def white_str(self):
        """
        Returns the Unicode character for a white king.

        Returns:
            str: The Unicode character for a white king.
        """
        return "♔"

    def black_str(self):
        """
        Returns the Unicode character for a black king.

        Returns:
            str: The Unicode character for a black king.
        """
        return "♚"

    # def possible_positions(self, row, col):
    #     """
    #     Calculates the possible positions the king can move to.

    #     Parameters:
    #         row (int): The current row of the king.
    #         col (int): The current column of the king.

    #     Returns:
    #         list: A list of tuples representing the possible positions the king can move to.
    #     """
    #     possibles = []

    #     directions = [
    #         (-1, 0), (1, 0), (0, -1), (0, 1),
    #         (-1, 1), (-1, -1), (1, 1), (1, -1)
    #     ]

    #     for dr, dc in directions:
    #         next_row, next_col = row + dr, col + dc
    #         if 0 <= next_row < 8 and 0 <= next_col < 8:
    #             possibles.append((next_row, next_col))

    #     return possibles

    def get_directions(self):
        return [(-1, 0), (1, 0), (0, -1), (0, 1),(-1, 1), (-1, -1), (1, 1), (1, -1)]