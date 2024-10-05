from game.piece import Piece

class InvalidCoordException(Exception):
    pass

class Rook(Piece):
    def white_str(self):
        return "♖"

    def black_str(self):
        return "♜"
   
    def possible_positions(self, row, col):
        possibles = []
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)] 

        for dr, dc in directions:
            next_row, next_col = row + dr, col + dc
            while 0 <= next_row < 8 and 0 <= next_col < 8:
                possibles.append((next_row, next_col))
                next_row += dr
                next_col += dc

        return possibles




    

