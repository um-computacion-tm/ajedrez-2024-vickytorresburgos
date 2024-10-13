from game.piece import Piece

class Bishop(Piece):
    def white_str(self):
        return "♗"

    def black_str(self):
        return "♝"
    
    # def possible_positions(self, row, col):

    #     """
    #     Calculate possible positions for a bishop given a starting position.

    #     Args: 
    #         row (int): The row of the starting position.
    #         col (int): The column of the starting position.

    #     Returns: 
    #         list: A list of tuples representing the possible positions.
    #     """
        
    #     possibles = []
        # directions = [(-1, 1), (-1, -1), (1, 1), (1, -1)]

    #     for dr, dc in directions:
    #         next_row, next_col = row + dr, col + dc
    #         while 0 <= next_row < 8 and 0 <= next_col < 8:
    #             possibles.append((next_row, next_col))
    #             next_row += dr
    #             next_col += dc

    #     return possibles

    def get_directions(self):
        return [(-1, 1), (-1, -1), (1, 1), (1, -1)]