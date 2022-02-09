from os import system, name

def main():
    time = True
    board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    has_winner = False
    is_draw = False
    
    while not has_winner:
        clear()
        print_board(board)
        
        print()
        
        play = ask_play(time)
        
        board[int(play) - 1] = "X" if time == True else "O"
        time = not time
        
        has_winner = has_win(board)
        is_draw = is_draw_(board)
        
        if is_draw:
            break
    
    clear()
    print_board(board)
    
    print()
    
    if not is_draw:
        print(("O" if time == True else "X") + " has won!")
    else:
        print("Draw!")

def is_draw_(board):
    count = 1
    for i in board:
        if i == str(count):
            return False
        
        count = count + 1
    
    return True

def ask_play(time):
    return input(("X" if time == True else "O") + " Turn | Play (1-9): ")

def clear():
    if name == "nt":
        _ = system("cls")
    else:
        _ = system("clear")

def print_board(board):
    print(" " + board[0] + " | " + board[1] + " | " + board[2])
    print("---+---+---")
    print(" " + board[3] + " | " + board[4] + " | " + board[5])
    print("---+---+---")
    print(" " + board[6] + " | " + board[7] + " | " + board[8])

def has_win(board):
    global is_draw
    
    if len(set([board[0], board[1], board[2]])) == 1:
        return True
    
    if len(set([board[3], board[4], board[5]])) == 1:
        return True
    
    if len(set([board[6], board[7], board[8]])) == 1:
        return True
    
    ####
    
    if len(set([board[0], board[3], board[6]])) == 1:
        return True
    
    if len(set([board[1], board[4], board[7]])) == 1:
        return True
    
    if len(set([board[2], board[5], board[8]])) == 1:
        return True
    
    ####
    
    if len(set([board[0], board[4], board[8]])) == 1:
        return True
    
    if len(set([board[2], board[4], board[6]])) == 1:
        return True
    
    # -------
    
    return False
    
if __name__ == "__main__":
    main()
