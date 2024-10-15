class Player:
    def __init__(self, color, pieces=16):
        """
        Initializes a new player.

        Parameters:
            color (str): The color of the player ("White" or "Black").
        """
        self.__color__ = color
        self.__pieces__ = pieces
        self.__score__ = 0
   
    @property
    def color(self):
        return self.__color__

    def sum_score(self, score):
        """
        Adds the given score to the player's score.

        Parameters:
            score (int): The score to add.
        """
        self.__score__ += score

    def remove_piece(self):
        """
        Removes one piece from the player's total pieces.
        """
        self.__pieces__ -= 1

    def has_pieces(self):
        """
        Checks if the player still has pieces remaining.

        Returns:
            bool: True if the player has at least one piece left, False otherwise.
        """
        return self.__pieces__ > 0
    
    @property
    def piece(self):
        return self.__pieces__
    
    @property
    def score(self):
        return self.__score__