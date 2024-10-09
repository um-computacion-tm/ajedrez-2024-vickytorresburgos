from game.piece import Piece

class Queen(Piece):
    def white_str(self):
        return "♕"

    def black_str(self):
        return "♛"

    def possible_positions(self, row, col):
        possibles = []

        directions = [
            (-1, 0), (1, 0), (0, -1), (0, 1), 
            (-1, 1), (-1, -1), (1, 1), (1, -1)  
        ]

        for dr, dc in directions:
            next_row, next_col = row + dr, col + dc
            while 0 <= next_row < 8 and 0 <= next_col < 8:
                other_piece = self.__board__.get_piece(next_row, next_col)
                if other_piece is not None:
                    if other_piece.__color__ != self.__color__:
                        possibles.append((next_row, next_col))
                    break
                possibles.append((next_row, next_col))
                next_row += dr
                next_col += dc

        return possibles  