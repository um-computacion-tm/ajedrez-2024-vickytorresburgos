from game.chess import Chess
from game.exceptions import EmptyPosition, InvalidDestination, InvalidMove, InvalidPawnMovement, InvalidTurn, OutOfBoard, PathBlocked

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
        print(f"Actual Turn: {chess.__actual_player__.color}") 
        print(f"Score Player 1: {chess.get_player(0).__score__}")
        print(f"Score Player 2: {chess.get_player(1).__score__}") 
        execute_play(chess)
    
        if not chess.get_player(0).has_pieces():
            print("Player 1 (White) has no pieces left! Player 2 (Black) wins!")
            break
        elif not chess.get_player(1).has_pieces():
            print("Player 2 (Black) has no pieces left! Player 1 (White) wins!")
            break

        player_1_response = input("Player 1 (White), do you want to end the game? (yes/no): ").strip().lower()
        player_2_response = input("Player 2 (Black), do you want to end the game? (yes/no): ").strip().lower()
        if chess.finish(player_1_response,player_2_response):
            print("The game ended by mutual agreement!")
            break

def execute_play(chess):
    try:
        from_row = int(input('From row (1-8): ')) - 1
        from_col = int(input('From col (1-8): ')) - 1
        to_row = int(input('To row (1-8): ')) - 1
        to_col = int(input('To col (1-8): ')) - 1
        chess.play(from_row, from_col, to_row, to_col)

    except ValueError:
        print('Unexpected input. Please try again')
    
    except (OutOfBoard, EmptyPosition, InvalidDestination, InvalidTurn, InvalidMove, PathBlocked, InvalidPawnMovement) as e:
        print(e.message) 
        print('Try again.')


if __name__ == '__main__':
    main()
