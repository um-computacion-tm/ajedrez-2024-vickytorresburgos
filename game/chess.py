from game.board import Board
from game.exceptions import EmptyPosition, InvalidDestination, InvalidMove, InvalidPawnMovement, InvalidTurn, OutOfBoard, PathBlocked
from game.knight import Knight
from game.pawn import Pawn
from game.player import Player

class Chess:
    def __init__(self):

        """
        Initializes a new chess game.

        This constructor sets up the players, the current player, and the chessboard.
        """
        self.players = [Player("White"), Player("Black")]
        self.actual_player = self.players[0]
        self.__board__ = Board()

    def is_playing(self): 

        """
        Checks if the game is still in progress.

        Returns:
            bool: True if the game is still in progress, False otherwise.
        """
        return True
    
    # el juego se termina si un jugador se queda sin fichas o si los jugadores 
    # deciden terminar la partida de mutuo acuerdo
    # -> si un jugador quiere terminar la partida, le tiene que preguntar al otro si tambien quiere terminarla?

    def validate_move(self, from_row, from_col,to_row,to_col):

        """
        Validates a move from one position to another on the chessboard.

        This function checks if the move is within the bounds of the board, if the origin
        position is not empty, if the piece belongs to the current player, if the destination
        position is valid, if the move is allowed for the piece, and if the path is not blocked.

        Parameters:
            from_row (int): The row index of the origin position.
            from_col (int): The column index of the origin position.
            to_row (int): The row index of the destination position.
            to_col (int): The column index of the destination position.

        Raises:
            OutOfBoard: If the destination position is out of the bounds of the chessboard.
            EmptyPosition: If the origin position is empty.
            InvalidTurn: If the piece at the origin position does not belong to the current player.
            InvalidDestination: If the destination position is occupied by a piece of the same color.
            InvalidMove: If the move is not allowed for the piece.
            InvalidPawnMovement: If a pawn is moving diagonally without capturing a piece.
            PathBlocked: If the path to the destination is blocked by another piece.
        """

        if not (0 <= to_row < 8 and 0 <= to_col < 8):
            raise OutOfBoard()
        
        origin_piece = self.__board__.get_piece(from_row, from_col) 
        
        if not origin_piece: 
            raise EmptyPosition()
        
        if not origin_piece.get_color() == self.actual_player.color: 
            raise InvalidTurn()

        destination_piece = self.__board__.get_piece(to_row,to_col) 

        if destination_piece and destination_piece.get_color() == self.actual_player.color: 
            raise InvalidDestination() 
        
        possible_positions = origin_piece.possible_positions(from_row, from_col) 
        if (to_row, to_col) not in possible_positions:
            raise InvalidMove() 
        
        if isinstance(origin_piece,Pawn) and from_col != to_col and not destination_piece: 
            raise InvalidPawnMovement() 
        
        if not isinstance(origin_piece, Knight):  
            direction = (to_row - from_row, to_col - from_col)
            steps = max(abs(direction[0]), abs(direction[1]))
            for i in range(1, steps):
                intermediate_row = from_row + (direction[0] * i // steps) 
                intermediate_col = from_col + (direction[1] * i // steps) 
                if self.__board__.get_piece(intermediate_row, intermediate_col) is not None: 
                    raise PathBlocked() 
                
    def get_player(self,index): 

        """
        Retrieves the player at the specified index.

        Parameters:
            index (int): The index of the player (0 for White, 1 for Black).

        Returns:
            Player: The player at the specified index.
        """

        return self.players[index]     
    
    def move(self,from_row,from_col, to_row, to_col):

        """
        Moves a piece from one position to another on the chessboard.

        This function validates the move, updates the board, updates the player's score if a piece
        is captured, removes the captured piece from the opponent's list, and changes the turn.

        Parameters:
            from_row (int): The row index of the origin position.
            from_col (int): The column index of the origin position.
            to_row (int): The row index of the destination position.
            to_col (int): The column index of the destination position.
        """

        self.validate_move(from_row, from_col, to_row, to_col) 
        destination = self.__board__.get_piece(to_row, to_col) 
        self.__board__.move(from_row, from_col, to_row, to_col) 

        if destination: 
            self.actual_player.sum_score(destination.get_score()) 
            if self.actual_player == self.get_player(1): 
                self.get_player(0).remove_piece() 
            else: 
                self.get_player(1).remove_piece() 
        self.change_turn() 
        

    def show_board(self):

        """
        Returns a string representation of the chessboard.

        Returns:
            str: A string representing the chessboard.
        """

        return str(self.__board__) 


    def change_turn(self):
        """
        Changes the turn to the other player.

        Returns:
            str: The color of the current player after changing the turn.
        """
        if self.actual_player == self.players[0]:
            self.actual_player = self.players[1]
        else:
            self.actual_player = self.players[0]
        return self.actual_player.color 