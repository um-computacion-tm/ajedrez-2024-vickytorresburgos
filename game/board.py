from game.rook import Rook
from game.knight import Knight
from game.bishop import Bishop
from game.queen import Queen
from game.king import King

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

        self.__positions__[0][0] = Rook("Black")
        self.__positions__[0][7] = Rook("Black") 
        self.__positions__[7][7] = Rook("White") 
        self.__positions__[7][0] = Rook("White") 
        self.__positions__[0][1] = Knight("Black")
        self.__positions__[0][6] = Knight("Black")
        self.__positions__[7][1] = Knight("White")
        self.__positions__[7][6] = Knight("White")
        self.__positions__[0][2] = Bishop("Black")
        self.__positions__[0][5] = Bishop("Black")
        self.__positions__[7][2] = Bishop("White")
        self.__positions__[7][5] = Bishop("White")
        self.__positions__[0][3] = Queen("Black")
        self.__positions__[7][3] = Queen("White")
        self.__positions__[0][4] = King("Black")
        self.__positions__[7][4] = King("White")

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




