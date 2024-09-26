from game.rook import Rook
from game.knight import Knight
from game.bishop import Bishop
from game.queen import Queen
from game.king import King
from game.pawn import Pawn

class InvalidMove(Exception):
    pass

class InvalidCoordException(Exception):
    pass

class OutOfBoard(Exception):
    message = "La posicion indicada se encuentra fuera del tablero"


class Board:
    def __init__(self, for_test = False):
        self.__positions__ = []
        for _ in range(8):
            col = []
            for _ in range(8):
                col.append(None)
            self.__positions__.append(col)
        if not for_test:
            self.__positions__[0][0] = Rook("Black",self)
            self.__positions__[0][7] = Rook("Black",self) 
            self.__positions__[7][7] = Rook("White",self) 
            self.__positions__[7][0] = Rook("White",self) 
            self.__positions__[0][1] = Knight("Black",self)
            self.__positions__[0][6] = Knight("Black",self)
            self.__positions__[7][1] = Knight("White",self)
            self.__positions__[7][6] = Knight("White",self)
            self.__positions__[0][2] = Bishop("Black",self)
            self.__positions__[0][5] = Bishop("Black",self)
            self.__positions__[7][2] = Bishop("White",self)
            self.__positions__[7][5] = Bishop("White",self)
            self.__positions__[0][3] = Queen("Black",self)
            self.__positions__[7][3] = Queen("White",self)
            self.__positions__[0][4] = King("Black",self)
            self.__positions__[7][4] = King("White",self)
            for i in range(8):
                self.__positions__[1][i] = Pawn("Black",self)
                self.__positions__[6][i] = Pawn("White",self)

    def __str__(self):
        board_str = ''
        for row in self.__positions__:
            row_str = ''
            for piece in row:
                if piece is None:
                    row_str += '  '  # Espacio para una casilla vacía
                else:
                    row_str += str(piece) + ' '  # Usamos el método __str__ de la pieza
            board_str += row_str + '\n'
        return board_str  
    
    def get_piece(self, row, col):
        if not (
            0 <= row < 8 or 0 <= col < 8
        ):
            raise OutOfBoard()
        return self.__positions__[row][col]
    
    def place_piece(self, row, col, piece):    
        self.__positions__[row][col] = piece

    def move(self, from_row, from_col, to_row, to_col):
        origin = self.get_piece(from_row, from_col)
        self.place_piece(to_row, to_col, origin)
        destination = self.get_piece(to_row, to_col)
        self.place_piece(from_row, from_col, None)

