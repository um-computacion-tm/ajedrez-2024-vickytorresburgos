class Player:
    def __init__(self, color):
        """
        Initializes a new player.

        Parameters:
            color (str): The color of the player ("White" or "Black").
        """
        self.color = color
        self.pieces = 16
        self.score = 0

    def sum_score(self, score):
        """
        Adds the given score to the player's score.

        Parameters:
            score (int): The score to add.
        """
        self.score += score

    def remove_piece(self):
        """
        Removes one piece from the player's total pieces.
        """
        self.pieces -= 1