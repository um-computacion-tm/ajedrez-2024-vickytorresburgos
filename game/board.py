from game.rook import Rook

class InvalidMoveException(Exception):
    pass

class InvalidCoordException(Exception):
    pass

class Board:
    def __init__(self):
        self.__positions__ = []
        for _ in range(8):
            col = []
            for _ in range(8):
                col.append(None)
            self.__positions__.append(col)

        self.__positions__[0][0] = Rook("Black") # Black
        self.__positions__[0][7] = Rook("Black") # Black
        self.__positions__[7][7] = Rook("White") # White
        self.__positions__[7][0] = Rook("White") # White

    def __str__(self):
        board_str = ""
        for row in self.__positions__:
            for cell in row:
                if cell is not None:
                    board_str += str(cell)
                else:
                    board_str += " "
            board_str += "\n"
        return board_str
    
    def get_piece(self, row, col):
        return self.__positions__[row][col]
    
    def place_piece(self, piece, row, col):
        self.__positions__[row][col] = piece




