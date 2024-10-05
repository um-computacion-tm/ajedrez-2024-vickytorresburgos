class InvalidMove(Exception):
    def __init__(self, message="The move is not valid"):
        self.message = message
        super().__init__(self.message)

class InvalidCoordException(Exception):
    def __init__(self, message="Invalid coordinates provided"):
        self.message = message
        super().__init__(self.message)

class InvalidTurn(Exception):
    def __init__(self, message="Invalid Turn. You cannot move your opponent's pieces"):
        self.message = message
        super().__init__(self.message)

class EmptyPosition(Exception):
    def __init__(self, message="The position is empty"):
        self.message = message
        super().__init__(self.message)

class OutOfBoard(Exception):
    def __init__(self, message="The position selected is out of the board"):
        self.message = message
        super().__init__(self.message)

class InvalidDestination(Exception):
    def __init__(self, message="The destination selected contains a piece of your own. Try again"):
        self.message = message
        super().__init__(self.message)

class PathBlocked(Exception):
    def __init__(self, message="There is a piece blocking the path"):
        self.message = message
        super().__init__(self.message)

class InvalidPawnMovement(Exception):
    def __init__(self, message="The pawn can only make a diagonal move to eat an opponents' piece"):
        self.message = message
        super().__init__(self.message)