class InvalidMove(Exception):
    message = "The move is not valid"
    def __str__(self):
        return self.message

class InvalidCoordException(InvalidMove):
    message = "Invalid coordinates provided"


class InvalidTurn(InvalidMove): #falta testear
    message="Invalid Turn. You cannot move your opponent's pieces"


class EmptyPosition(InvalidMove):
    message="The position is empty" #falta testear


class OutOfBoard(InvalidMove):
    message="The position selected is out of the board"


class InvalidDestination(InvalidMove):
    message="The destination selected contains a piece of your own. Try again"

class PathBlocked(InvalidMove): #falta testear
    message="There is a piece blocking the path"


class InvalidPawnMovement(InvalidMove):
    message="The pawn can only make a diagonal move to eat an opponents' piece" #falta testear