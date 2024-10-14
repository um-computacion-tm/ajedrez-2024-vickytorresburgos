from game.piece import Piece

class Pawn(Piece):
    
    def white_str(self):
        """
        Returns the Unicode character for a white pawn.

        Returns:
            str: The Unicode character for a white pawn.
        """
        return "♙"

    def black_str(self):
        """
        Returns the Unicode character for a black pawn.

        Returns:
            str: The Unicode character for a black pawn.
        """
        return "♟"

    def possible_positions(self, row, col, directions, more_than_one_step):
        """
        Calculates the possible positions the pawn can move to.

        Parameters:
            row (int): The current row of the pawn.
            col (int): The current column of the pawn.

        Returns:
            list: A list of tuples representing the possible positions the pawn can move to.
        """
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

