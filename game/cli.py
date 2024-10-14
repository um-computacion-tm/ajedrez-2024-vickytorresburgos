from game.chess import Chess
from game.exceptions import EmptyPosition, InvalidDestination, InvalidMove, InvalidPawnMovement, InvalidTurn, OutOfBoard, PathBlocked
# from colorama import Fore

def main():

    """
    The main function to start and run the chess game.

    This function initializes the chess game, prints the initial state of the board, and enters a loop
    where it continuously prompts the players to make moves until the game is over. It also displays
    the current player's turn and the scores of both players.
    """

    chess = Chess()
    print("Starting Chess Game!!!")
    print("Enter the position in which you want to place your piece")
    while chess.is_playing():
        print(chess.show_board())
        print(f"Actual Turn: {chess.actual_player.color}") 
        print(f"Score Player 1: {chess.get_player(0).score}")
        print(f"Score Player 2: {chess.get_player(1).score}") 
        play(chess)
    
    # le tiene que preguntar en cada ronda al jugador si quiere seguir jugando? 
    # ver puntuacion

def play(chess):

    """
    Handles the player's move input and updates the game state.

    This function prompts the player to enter the positions for the move, validates the input, and
    updates the game state accordingly. If the input is invalid or an exception is raised, it catches
    the exception and prompts the player to try again.

    Parameters:
        chess (Chess): The chess game object.
    """

    try:
        from_row = int(input('From row (1-8): ')) - 1
        from_col = int(input('From col (1-8): ')) - 1
        to_row = int(input('To row (1-8): ')) - 1
        to_col = int(input('To col (1-8): ')) - 1
        chess.move(from_row, from_col, to_row, to_col)

    except ValueError:
        print('Unexpected input. Please try again')
    
    except (OutOfBoard, EmptyPosition, InvalidDestination, InvalidTurn, InvalidMove, PathBlocked, InvalidPawnMovement) as e:
        print(e.message) 
        print('Try again.')

if __name__ == '__main__':
    main()
