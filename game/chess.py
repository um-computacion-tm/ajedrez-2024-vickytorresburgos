from game.board import Board,InvalidMove
from game.player import Player

class InvalidTurn(Exception):
    message = "Invalid Turn. You cannot move your opponent's pieces"

class EmptyPosition(Exception):
    message = "The position is empty"

class OutOfBoard(Exception):
    message = "The position selected is out of the board"

class Chess:
    def __init__(self):
        self.__board__ = Board()
        self.players = [Player("White"), Player("Black")]
        self.actual_player = self.players[0]

    def is_playing(self):

        return True
    
    #false si uno de los jugadores desea terminar la partida o uno de los jugadores se queda sin fichas

    def move(self,from_row,from_col,to_row,to_col):
        piece = self.__board__.get_piece(from_row, from_col)
        if not piece:
            raise EmptyPosition()
        if not piece.get_color() == self.actual_player.color:
            raise InvalidTurn()
        if not (0 <= to_row < 8 and 0 <= to_col < 8):
            raise OutOfBoard()
        # if not piece.valid_positions(from_row, from_col, to_row, to_col):
        #     raise InvalidMove()
        self.__board__.move(from_row, from_col, to_row, to_col)

    @property
    def show_board(self):
        return str(self.__board__)

    def change_turn(self):
        if self.actual_player.color == "White":
            self.actual_player = self.players[1]
        else:
            self.actual_player = self.players[0]

# agregar metodo validate move que valide el movimiento

# posicion este disponible, este vacia
# pieza sea de su color
# si hay una pieza en donde quiere poner la pieza, verificar que sea del otro color
# ingrese un numero 
# ingrese una posicion dentro del tablero
# movimiento de la ficha sea valido (torre en horizontal y vertical, alfil en diagonal, etc)

# hacer metodo que una vez que se haya validado el movimiento, mueva la ficha
# y cambie de turno