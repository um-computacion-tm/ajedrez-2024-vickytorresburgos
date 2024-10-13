from game.piece import Piece

class Knight(Piece):
    def white_str(self):
        """
        Returns the Unicode character for a white knight.

        Returns:
            str: The Unicode character for a white knight.
        """
        return "♘"

    def black_str(self):
        """
        Returns the Unicode character for a black knight.

        Returns:
            str: The Unicode character for a black knight.
        """
        return "♞"

    # def possible_positions(self, row, col):
    #     """
    #     Calculates the possible positions the knight can move to.

    #     Parameters:
    #         row (int): The current row of the knight.
    #         col (int): The current column of the knight.

    #     Returns:
    #         list: A list of tuples representing the possible positions the knight can move to.
    #     """
    #     possibles = []

    #     directions = [
    #         (-2, 1), (-2, -1), (2, 1), (2, -1),
    #         (1, 2), (-1, 2), (1, -2), (-1, -2)
    #     ]

    #     for dr, dc in directions:
    #         next_row, next_col = row + dr, col + dc
    #         if 0 <= next_row < 8 and 0 <= next_col < 8:
    #             possibles.append((next_row, next_col))

    #     return possibles

    def get_directions(self):
        return  [(-2, 1), (-2, -1), (2, 1), (2, -1),(1, 2), (-1, 2), (1, -2), (-1, -2)]