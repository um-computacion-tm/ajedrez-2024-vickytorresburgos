from game.chess import Chess
from game.board import Board

class RangeError(Exception):
    pass

def main():
    board = Board()
    print(board)
    chess = Chess()
    while chess.is_playing():
        play(chess)
    

def play(chess):
    try:
        print("turn: ", chess.turn)
        from_row = int(input('From row: '))
        validate_input(from_row)
        
        from_col = int(input('From col: '))
        validate_input(from_col)

        to_row = int(input('To row: '))
        validate_input(to_row)

        to_col = int(input('To col: '))
        validate_input(to_col)

        chess.move(
            from_row,
            from_col,
            to_row,
            to_col,
        ) 
    
    except ValueError:
        print('Unexpected input. Please try again')
    
    except RangeError:
        print('Coords out of range. Please try again')
        
def validate_input(value):
    if value < 1 or value > 8:
        raise RangeError

if __name__ == '__main__':
    main()
