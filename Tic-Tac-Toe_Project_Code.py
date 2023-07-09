from IPython.display import clear_output
def display_board(board):
    clear_output()
    print(board[7]+"|"+board[8]+"|"+board[9])
    print(board[4]+"|"+board[5]+"|"+board[6])
    print(board[1]+"|"+board[2]+"|"+board[3])
def player_input():
    a=''
    while a!='X' and a!='O':
        a = input("Player 1 enter X or O:")
    player1=a
    if player1=="X":
        player2="O"
    else:
        player2="X"
    return (player1,player2)
def place_marker(board,marker,position):
    board[position]=marker
    return board
def win_check(board,mark):
    a=['X']*3
    b=['O']*3
    if mark=="X":
        return board[1:4] == a or board[4:7] == a or board[7:10] == a or board[1:8:3] == a or board[2:9:3] == a or board[3:10:3] == a or board[3:8:2] == a or board[1:10:4] == a
    if mark=="O":
        return board[1:4] == b or board[4:7] == b or board[7:10] == b or board[1:8:3] == b or board[2:9:3] == b or board[3:10:3] == b or board[3:8:2] == b or board[1:10:4] == b
import random
def choice_first():
    first=random.randint(1,2)
    if first==1:
        return "Player 1"
    else:
        return "Player 2"
def space_check(board,position):
    return board[position]==" "
def full_board_check(board):
    return " " not in board
def player_choice(board):
    if full_board_check(board)==False:
        position=0
        while position not in [1,2,3,4,5,6,7,8,9] or space_check(board,position)==False:
            position=int(input("Choose position from 1 to 9 which are not choosen earlier:"))
        return position
    else:
        return "It is full.I can not take more entry"
def replay():
    a=""
    while a!="Y" and a!="N":
        a = input("Do you want to play again? Choose Y or N:")
    return a=="Y"
print("Welcome to Tic Tac Toe!")
def game_on():
    board = ["#", " ", " ", " ", " ", " ", " ", " ", " ", " "]
    turn=choice_first()
    print(turn+" will go first")
    player1, player2 = player_input()
    count = 0
    if turn=="Player 1":
        while count < 9:
            position = player_choice(board)
            count += 1
            if count % 2 == 1:
                marker = player1
            else:
                marker = player2
            place_marker(board, marker, position)
            display_board(board)
            if win_check(board, player1):
                print("Player 1 has won this match")
                break
                print("Player 2 has won this match")
                break
            else:
                pass
    else:
        while count < 9:
            position = player_choice(board)
            count += 1
            if count % 2 == 1:
                marker = player2
            else:
                marker = player1
            place_marker(board, marker, position)
            display_board(board)
            if win_check(board, player1):
                print("Player 1 has won this match")
                break
            elif win_check(board, player2):
                print("Player 2 has won this match")
                break
            else:
                pass
    if win_check(board,marker)==False:
        print("It is a tie")
game_on()
while True:
    if replay():
        game_on()
    else:
        break