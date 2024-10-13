from game.piece import Piece

class Rook(Piece):
    def white_str(self):
        """
        Returns the Unicode character for a white rook.

        Returns:
            str: The Unicode character for a white rook.
        """
        return "♖"

    def black_str(self):
        """
        Returns the Unicode character for a black rook.

        Returns:
            str: The Unicode character for a black rook.
        """
        return "♜"

    # def possible_positions(self, row, col):
    #     """
    #     Calculates the possible positions the rook can move to.

    #     Parameters:
    #         row (int): The current row of the rook.
    #         col (int): The current column of the rook.

    #     Returns:
    #         list: A list of tuples representing the possible positions the rook can move to.
    #     """        
    #     possibles = []
    #     directions = [(-1, 0), (1, 0), (0, -1), (0, 1)] 

    #     for dr, dc in directions:
    #         next_row, next_col = row + dr, col + dc
    #         while 0 <= next_row < 8 and 0 <= next_col < 8:
    #             possibles.append((next_row, next_col))
    #             next_row += dr
    #             next_col += dc
    #     return possibles
    
    def get_directions(self):
        return [(-1, 0), (1, 0), (0, -1), (0, 1)]


    

