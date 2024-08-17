from game.chess import Chess

def main():
    chess = Chess()
    while True:
        play(chess)

def validate_input(value):
    try:
        number = int(value)
        if number < 0 or number > 8:
            raise ValueError
    except ValueError:
        raise ValueError("Invalid input. Please enter a number between 0 and 8.")
    return number

def play(chess):
    try:
        print("turn: ", chess.turn)
        from_row = int(input('From row: ')) 
        from_col = int(input('From col: ')) 
        to_row = int(input('To row: ')) 
        to_col = int(input('To col: ')) 
  
        chess.move(
            from_row,
            from_col,
            to_row,
            to_col,
        ) 
        
    except ValueError as e:
        print(f"Error de entrada: {e}")

if __name__ == '__main__':
    main()
