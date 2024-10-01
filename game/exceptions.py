class InvalidMove(Exception):
    pass

class InvalidCoordException(Exception):
    pass

class InvalidTurn(Exception):
    message = "Invalid Turn. You cannot move your opponent's pieces"

class EmptyPosition(Exception):
    message = "The position is empty"

class OutOfBoard(Exception):
    message = "The position selected is out of the board"

class InvalidDestination(Exception):
    message = "The destination selected contains a piece of your own. Try again"

class PathBlocked(Exception):
    message = "There is a piece blocking the path"
