from game.piece import Piece

class Knight(Piece):
    def white_str(self):
        return "♘"

    def black_str(self):
        return "♞"

    def possible_positions(self, row, col):
        possibles = []

        directions = [
            (-2, 1), (-2, -1), (2, 1), (2, -1),
            (1, 2), (-1, 2), (1, -2), (-1, -2)
        ]

        for dr, dc in directions:
            next_row, next_col = row + dr, col + dc
            if 0 <= next_row < 8 and 0 <= next_col < 8:
                other_piece = self.__board__.get_piece(next_row, next_col)
                if other_piece is None or other_piece.__color__ != self.__color__:
                    possibles.append((next_row, next_col))

        return possibles