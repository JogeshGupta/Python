"""Project-1: Tic-Tac-Toe Game in Python
Task Details: 
You will create a Tic-Tac-Toe game where two players (Player X and Player O) take 
turns to mark a 3x3 grid with their respective symbols ("X" or "O"). The game ends when 
one player wins by aligning their symbols in a row, column, or diagonal, or when the 
game results in a tie.
"""


"""1. Create the Tic-Tac-Toe board: 
o Use a list of 9 elements (initialized with empty spaces) to represent the 3x3 
grid. 
o Write a function print_board() to display the current state of the board."""


def print_board(board):

    print()
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print()

"""2. Game Logic: 
o Implement a function to check if a player has won. A player wins if they have 
filled any one of the following combinations with their symbol: 
 Rows: [0, 1, 2], [3, 4, 5], [6, 7, 8] 
 Columns: [0, 3, 6], [1, 4, 7], [2, 5, 8] 
 Diagonals: [0, 4, 8], [2, 4, 6] 
o Implement a function to check if the game has resulted in a tie (i.e., all 
positions are filled, and no player has won). """

def check_winner(board, player):
    """Returns true if player has filled any row, column or diagonal"""

    winning_combinations = [
        [0,1,2], [3,4,5], [6,7,8],  
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6],
    ]
    for combo in winning_combinations:
        #checks if all 3 pos holds player's symbol
        if all(board[i] == player for i in combo):
            return True
    return False    


def check_tie(board):
#returns true if every pos filled called after checking winner

    return " " not in board

"""3. Handle Player Input: 
o Write a function that asks the current player to choose a position (1-9) on the 
board. 
o Validate that the input is a number between 1 and 9 and that the chosen 
position is not already taken."""


def get_player_input(player, board):

    while True:
        choice = input(f"Player {player}, choose a position(1-9): ").strip()

        #validate : must be a number
        if not choice.isdigit():
            print("Invalid input! Please enter a number between 1 and 9.")
            continue

        position = int(choice)

        #validate: must be in range 1-9
        if position < 1 or position > 9:
            print("Invalid input! Position must be between 1 and 9.")
            continue

        #validate: position must not be already taken
        if board[position - 1] != " ":
            print("That position is already taken. Try another one.")
            continue

        return position - 1  # "-1" for converting 1-9 to 0-8

    
#4. Main game logic

def play_game():

    print("Welcome to Tic-Tac-Toe!")

    while True: #outer loop: allows replaying
        board = [" "]*9 #new empty board
        current_player = "X" # X always starts
        print_board(board)

        while True: # inner loop : 1 full game
            #getting move and palcing symbol
            index = get_player_input(current_player, board)
            board[index] = current_player
            print_board(board)

            #check if the current player won
            if check_winner(board, current_player):
                print(f"Congratulations! Player {current_player} wins!")
                break

            #check for tie
            if check_tie(board):
                print("It's a tie!")
                break

            #switch turns
            current_player = "O" if current_player == "X" else "X"

        # replay option
        again = input("Do you want to play again? (yes/no): ").strip().lower()
        if again != "yes":
            print("Thanks for playing! see ya later")
            break

play_game()