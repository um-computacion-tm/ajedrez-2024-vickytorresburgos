from game.board import Board,InvalidMove
from game.player import Player

class InvalidTurn(Exception):
    message = "Invalid Turn. You cannot move your opponent's pieces"

class EmptyPosition(Exception):
    message = "The position is empty"

class OutOfBoard(Exception):
    message = "The position selected is out of the board"

class InvalidDestination(Exception):
    message = "The destination selected contains a piece of your own. Try again"

class Chess:
    def __init__(self):
        self.__board__ = Board()
        self.players = [Player("White"), Player("Black")]
        self.actual_player = self.players[0]

    def is_playing(self):
        return True
    
    # el juego se termina si un jugador se queda sin fichas o si los jugadores 
    # deciden terminar la partida de mutuo acuerdo
    # -> si un jugador quiere terminar la partida, le tiene que preguntar al otro si tambien quiere terminarla?

    def validate_move(self, from_row, from_col,to_row,to_col):
        if not (0 <= to_row < 8 and 0 <= to_col < 8):
            raise OutOfBoard()
        
        origin_piece = self.__board__.get_piece(from_row, from_col)
        
        if not origin_piece:
            raise EmptyPosition()
        
        if not origin_piece.get_color() == self.actual_player.color:
            raise InvalidTurn()
        
        # pieza se puede mover a esa posicion


        # falta validacion de que no haya una ficha en el medio entre el origen y el destino

        destination_piece = self.__board__.get_piece(to_row,to_col)

        if destination_piece:
            if destination_piece.get_color() == self.actual_player.color:
                raise InvalidDestination()
            
    def get_player(self,index):
        return self.players[index]     
    
    def move(self,from_row,from_col, to_row, to_col):
        self.validate_move(from_row, from_col, to_row, to_col)
        destination = self.__board__.get_piece(to_row, to_col)
        self.__board__.move(from_row, from_col, to_row, to_col)

        if destination:
            self.actual_player.sum_score(destination.get_score())
            if self.actual_player == self.get_player(1):
                self.get_player(0).remove_piece()
            else:
                self.get_player(1).remove_piece()

    @property
    def show_board(self):
        return str(self.__board__)

    def change_turn(self):
        if self.actual_player.color == "White":
            self.actual_player = self.players[1]
        else:
            self.actual_player = self.players[0]