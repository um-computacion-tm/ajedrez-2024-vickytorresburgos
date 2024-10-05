class Player():
    def __init__(self, color):
        self.color = color
        self.pieces = 16
        self.score = 0

    def sum_score(self, score):
        self.score += score

    def remove_piece(self):
        self.pieces -= 1