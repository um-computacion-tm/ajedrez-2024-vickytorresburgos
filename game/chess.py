from game.board import Board,InvalidMove

class InvalidTurn(Exception):
    message = "No puedes mover pieza de otro jugador"

class EmptyPosition(Exception):
    message = "La posicion esta vacia"

class OutOfBoard(Exception):
    message = "La posicion indicada se encuentra fuera del tablero"

class Chess:
    def __init__(self):
        self.__board__ = Board()
        self.__turn__= "White"

    def is_playing(self):
        return True
        
    def move(self,from_row,from_col,to_row,to_col):
        self.change_turn()

        piece = self.__board__.get_piece(from_row, from_col)
        if not piece:
            raise EmptyPosition()
        if not piece.get_color() == self.__turn__:
            raise InvalidTurn()
        if not piece.valid_positions(from_row, from_col, to_row, to_col):
            raise InvalidMove()
        self.__board__.move(from_row, from_col, to_row, to_col)
        self.change_turn()
   
    @property
    
    def turn(self):
         return self.__turn__
    
    def show_board(self):
        return str(self.__board__)
    
    def change_turn(self):
        if self.__turn__ == "White":
            self.__turn__ = "Black"
        else:
            self.__turn__ = "White"
