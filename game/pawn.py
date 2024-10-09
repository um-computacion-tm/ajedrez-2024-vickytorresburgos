from game.piece import Piece

class Pawn(Piece):
    def white_str(self):
        return "♙"

    def black_str(self):
        return "♟"
    
    def possible_positions(self, row, col):
        possibles = []
        direction = -1 if self.__color__ == "White" else 1
        if 0 <= row + direction < 8:
            possibles.append((row + direction, col))
            
            if (self.__color__ == "White" and row == 6) or (self.__color__ == "Black" and row == 1):
                possibles.append((row + 2 * direction, col))
       
        for dc in [-1, 1]:
            if 0 <= row + direction < 8 and 0 <= col + dc < 8:
                piece = self.__board__.get_piece(row + direction, col + dc)
                if piece and piece.get_color() != self.get_color():
                    possibles.append((row + direction, col + dc)) 
        return possibles

