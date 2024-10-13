from game.rook import Rook
from game.knight import Knight
from game.bishop import Bishop
from game.queen import Queen
from game.king import King
from game.pawn import Pawn
from game.exceptions import OutOfBoard


class Board:
    def __init__(self,for_test = False):
        """
        Initializes a board with the pieces in their starting positions.

        Parameters:
            for_test (Bool) = If True, the board initializes empty, used only for testing purposes. 
            if False, the board initializes with the pieces in their starting positions.

        Attributes:
            __positions__ (list): List representing the board, where every element is either a piece object or None
        """
        self.__positions__ = []
        for _ in range(8):
            col = []
            for _ in range(8):
                col.append(None)
            self.__positions__.append(col)
        if not for_test:
            self.__positions__[0][0] = Rook("Black",self,5)
            self.__positions__[0][7] = Rook("Black",self,5) 
            self.__positions__[7][7] = Rook("White",self,5) 
            self.__positions__[7][0] = Rook("White",self,5) 
            self.__positions__[0][1] = Knight("Black",self,3)
            self.__positions__[0][6] = Knight("Black",self,3)
            self.__positions__[7][1] = Knight("White",self,3)
            self.__positions__[7][6] = Knight("White",self,3)
            self.__positions__[0][2] = Bishop("Black",self,3)
            self.__positions__[0][5] = Bishop("Black",self,3)
            self.__positions__[7][2] = Bishop("White",self,3)
            self.__positions__[7][5] = Bishop("White",self,3)
            self.__positions__[0][3] = Queen("Black",self,9)
            self.__positions__[7][3] = Queen("White",self,9)
            self.__positions__[0][4] = King("Black",self,1)
            self.__positions__[7][4] = King("White",self,1)
            for i in range(8):
                self.__positions__[1][i] = Pawn("Black",self,1)
                self.__positions__[6][i] = Pawn("White",self,1)

    def __str__(self):
        """
        Generates a string representation of the chessboard.

        This function iterates through the matrix of positions on the chessboard and constructs a string
        that visually represents the current state of the board. Each piece is represented by its corresponding
        symbol, and empty squares are represented by spaces.

        Returns:
            str: A string representing the chessboard.
        """
        board_str = ''
        for row in self.__positions__:
            row_str = ''
            for piece in row:
                if piece is None:
                    row_str += '  ' 
                else:
                    row_str += str(piece) + ' ' 
            board_str += row_str + '\n'
        return board_str  
    
    def get_piece(self, row, col): #codigo duplicado
        
        """
    Retrieves the piece at the specified position on the chessboard.

    This function checks if the given row and column indices are within the bounds of the chessboard.
    If the indices are valid, it returns the piece at the specified position. If the indices are out of
    bounds, it raises an OutOfBoard exception.

    Parameters:
        row (int): The row index of the position.
        col (int): The column index of the position.

    Returns:
        Piece: The piece at the specified position.

    Raises:
        OutOfBoard: If the row or column index is out of the bounds of the chessboard.
    """
        return self.__positions__[row][col]
    
    def place_piece(self, row, col, piece): #codigo duplicados
        """
    Places a piece at the specified position on the chessboard.

    This function sets the piece at the specified row and column indices on the chessboard.

    Parameters:
        row (int): The row index of the position.
        col (int): The column index of the position.
        piece (Piece): The piece to be placed at the specified position.
        """
        self.__positions__[row][col] = piece

    def move(self, from_row, from_col, to_row, to_col):

        """
    Moves a piece from one position to another on the chessboard.

    This function retrieves the piece from the origin position, places it at the destination position,
    and sets the origin position to None.

    Parameters:
        from_row (int): The row index of the origin position.
        from_col (int): The column index of the origin position.
        to_row (int): The row index of the destination position.
        to_col (int): The column index of the destination position.
        """
        
        origin = self.get_piece(from_row, from_col)
        self.place_piece(to_row, to_col, origin)
        self.place_piece(from_row, from_col, None)

