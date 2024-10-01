class Piece:
    def __init__(self, color, board, score):
        self.__color__ = color
        self.__board__ = board
        self.__score__ = score

    def white_str(self):
        return ""

    def black_str(self):
        return ""

    def __str__(self):
        if self.__color__ == "White":
            return self.white_str()
        else:
            return self.black_str()

    def get_color(self):
        return self.__color__

    def get_score(self):
        return self.__score__
    
