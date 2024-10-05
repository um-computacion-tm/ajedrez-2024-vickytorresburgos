from game.chess import Chess
from game.exceptions import EmptyPosition, InvalidDestination, InvalidMove, InvalidPawnMovement, InvalidTurn, OutOfBoard, PathBlocked

def main():
    chess = Chess()
    print("Starting Chess Game!!!")
    while chess.is_playing():
        print(chess.show_board())
        print(f"Actual Turn: {chess.actual_player.color}")  # Imprime el turno antes de jugar
        play(chess)
        chess.change_turn()
    
    # le tiene que preguntar en cada ronda al jugador si quiere seguir jugando? 
    # ver puntuacion

def play(chess):
    while True:
        try:
            from_row = int(input('From row: ')) - 1
            from_col = int(input('From col: ')) - 1
            to_row = int(input('To row: ')) - 1
            to_col = int(input('To col: ')) - 1
            chess.move(from_row, from_col, to_row, to_col)
            break

        except ValueError:
            print('Unexpected input. Please try again')
        
        except (OutOfBoard, EmptyPosition, InvalidDestination, InvalidTurn, InvalidMove, PathBlocked, InvalidPawnMovement) as e:
                print(e.message) 
                print('Try again.')
                print(chess.show_board())  

if __name__ == '__main__':
    main()
