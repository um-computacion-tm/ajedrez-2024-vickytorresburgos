from game.board import Board
from game.exceptions import EmptyPosition, InvalidDestination, InvalidMove, InvalidTurn, OutOfBoard, PathBlocked
from game.knight import Knight
from game.player import Player

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

        destination_piece = self.__board__.get_piece(to_row,to_col)

        if destination_piece:
            if destination_piece.get_color() == self.actual_player.color:
                raise InvalidDestination()

        
        possible_positions = origin_piece.possible_positions(from_row, from_col)
        if (to_row, to_col) not in possible_positions:
            raise InvalidMove()

     #  Verificar que no haya una ficha en el medio entre el origen y el destino
        if not isinstance(origin_piece, Knight):  # El caballo puede saltar
            direction = (to_row - from_row, to_col - from_col)
            steps = max(abs(direction[0]), abs(direction[1]))
            for i in range(1, steps):
                intermediate_row = from_row + (direction[0] * i // steps)
                intermediate_col = from_col + (direction[1] * i // steps)
                if self._board_.get_piece(intermediate_row, intermediate_col) is not None:
                    raise PathBlocked()

            
    def get_player(self,index): 
        return self.players[index]  # falta testear    
    
    def move(self,from_row,from_col, to_row, to_col):
        self.validate_move(from_row, from_col, to_row, to_col)
        destination = self.__board__.get_piece(to_row, to_col)
        self.__board__.move(from_row, from_col, to_row, to_col)

        if destination:
            self.actual_player.sum_score(destination.get_score()) # falta testear
            if self.actual_player == self.get_player(1):
                self.get_player(0).remove_piece()
            else:
                self.get_player(1).remove_piece()

    # @property
    def show_board(self):
        return str(self.__board__) # falta testear


    def change_turn(self):
        if self.actual_player.color == "White":
            self.actual_player = self.players[1] # falta testear
        else:
            self.actual_player = self.players[0]