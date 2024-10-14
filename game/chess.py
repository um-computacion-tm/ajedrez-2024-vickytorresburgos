from game.board import Board
from game.exceptions import EmptyPosition, InvalidDestination, InvalidMove, InvalidPawnMovement, InvalidTurn, OutOfBoard, PathBlocked
from game.knight import Knight
from game.pawn import Pawn
from game.player import Player
from game.king import King
from game.queen import Queen
from game.bishop import Bishop

class Chess:
    def __init__(self):

        """
        Initializes a new chess game.

        This constructor sets up the players, the current player, and the chessboard.
        """
        self.players = [Player("White"), Player("Black")]
        self.actual_player = self.players[0]
        self.__board__ = Board()
        self.agreed_draw = False

    def is_playing(self): 
        """
        Checks if the game is still in progress based on the following conditions:
        
        1. A player has no pieces left.
        2. Players decide to end the game by mutual agreement.
        
        Returns:
            bool: True if the game is still in progress, False otherwise.
        """
        for player in self.players:
            if not player.has_pieces():
                print(f"{player.color} has no pieces left. Game Over!")
                return False
        if self.agreed_draw:
            print("Game ended by mutual agreement.")
            return False
        return True
    
    def end_game_by_agreement(self):
            """
            Allows players to end the game by mutual agreement.
            """
            self.agreed_draw = True

    def validate_move(self, from_row, from_col,to_row,to_col):

        """
    Validates if a move from the origin position to the destination position is legal.

    Args:
        from_row (int): The row index of the piece's origin position.
        from_col (int): The column index of the piece's origin position.
        to_row (int): The row index of the destination position.
        to_col (int): The column index of the destination position.

    Raises:
        OutOfBoard: If the destination coordinates are out of the board's boundaries.
        EmptyPosition: If there is no piece at the origin position.
        InvalidTurn: If the piece at the origin does not belong to the current player.
        InvalidDestination: If the destination square contains a piece of the same color.
        InvalidMove: If the destination is not in the piece's valid possible positions.
        InvalidPawnMovement: If a pawn tries to capture by moving forward instead of diagonally.
        PathBlocked: If a non-Knight piece's path to the destination is blocked by another piece.
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
        
        directions, more_than_one_step = self.movement(origin_piece)
        possible_positions = origin_piece.possible_positions(from_row, from_col, directions, more_than_one_step) 
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
                
    def movement(self, piece):
        """
    Determines the valid movement directions for a given chess piece.

    Args:
        piece (Piece): The chess piece for which to determine valid movement directions.

    Returns:
        tuple: A tuple containing:
            - directions (list of tuple): A list of relative (row, col) movement directions.
            - more_than_one_step (bool): A flag indicating whether the piece can move multiple steps.

    Notes:
        - Knights have an "L" shaped movement pattern and are not restricted by blocking pieces.
        - Queens can move in any direction and for multiple steps.
        - Kings can move one step in any direction.
        - Bishops can move diagonally for multiple steps.
        - Rooks and Pawns move forward and sideways (Pawns also move diagonally when capturing).
    """
        if isinstance(piece, King) or isinstance(piece, Queen) or isinstance(piece, Knight):
            return  [(-2, 1), (-2, -1), (2, 1), (2, -1), (1, 2), (-1, 2), (1, -2), (-1, -2)] if isinstance(piece, Knight) else [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, 1), (-1, -1), (1, 1), (1, -1)], True if isinstance(piece, Queen) else False 
        elif isinstance(piece, Bishop):
            return [(-1, 1), (-1, -1), (1, 1), (1, -1)], True 
        else:
            return [(-1, 0), (1, 0), (0, -1), (0, 1)], True

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

        if not self.actual_player.has_pieces():
            print(f"{self.actual_player.color} has no pieces left. Game Over!")
        
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