from game.piece import Piece

class Rook(Piece):
    def __init__(self, color):
        self.color = color

    # def valid_move(self,from_col,to_col,from_row,to_row,board):
    #     if from_row == to_row or from_col == to_col:
    #         if self.is_path_clear(from_row, from_col, to_row, to_col, board):
    #             return True
    #         return False
        