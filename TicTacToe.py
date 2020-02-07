# Game Board

temp_board = ["1","2","3","4","5","6","7","8","9"]

board = ["_","_","_","_","_","_","_","_","_"]

# Display of Board

def temp_board_display():
    print(temp_board[0] + "|" + temp_board[1] + "|" + temp_board[2])
    print(temp_board[3] + "|" + temp_board[4] + "|" + temp_board[5])
    print(temp_board[6] + "|" + temp_board[7] + "|" + temp_board[8])
    print("\n")
    

def board_display():
    print(board[0]  +  "|"  +  board[1]  +  "|"  +  board[2])
    print(board[3]  +  "|"  +  board[4]  +  "|"  +  board[5])
    print(board[6]  +  "|"  +  board[7]  +  "|"  +  board[8])


# Processing of Game
game_running  =  True

# Win or Tie
winner  =  None

# Who's Turn
player  =  "X"


# Changing the Player
        
def change_player():
    global player
    
    if (player == "X"):
        player = "O"
    elif (player == "O"):
        player = "X"
        
    return

# Definition of Turns
 
def turn(player):
    print(player,"'s Turn")
    pos  =  int(input("Choose a Spot on Board from 1-9 : "))
    
    if pos not in range (1,10):
        print("Invalid Spot")
        pos  =  int(input("Choose a Spot on Board from 1-9 : "))
    
    pos  =  pos - 1
    
    if (board[pos]  !=  "_"):
        print("Choose again")
        pos = int(input("Choose a Spot on Board from 1-9 : "))
        
    board[pos]  =  player
    board_display()
    
    
# Running of Game
    
def game():
    
    temp_board_display()
    
    board_display()
   
    
    # When Game is still Going
    while game_running:
        
        # Check the Turn of the Player
        turn(player)
        
        # Check if the Game is Over
        check_game_over()
        
        # Change the Player
        change_player()
        
    # Game Over
    if (winner == "X" or winner == "O"):
        print(winner," Won")
    elif (winner == None):
        print("Game is Tie")


# Check if the Game is over or not
        
def check_game_over():
    check_win()
    check_tie()
    
    
# Check for the Winner
    
def check_win():
    
    global winner
    
    # check rows
    row_win  =  check_rows()
    # check columns
    column_win  =  check_columns()
    # check diagonals
    diagonal_win  =  check_diagonals()
    
    
    if (row_win):
        winner  =  row_win
    elif (column_win):
        winner  =  column_win
    elif (diagonal_win):
        winner  =  diagonal_win
    else :
        winner = None
        
    return 


# Checking of Rows for Win
    
def check_rows():
    
    global game_running
    
    row1  =  board[0]  ==  board[1]  ==  board[2] != "_"
    row2  =  board[3]  ==  board[4]  ==  board[5] != "_"
    row3  =  board[6]  ==  board[7]  ==  board[8] != "_"
    
    if (row1 or row2 or row3):
        game_running = False
        
    if (row1):
        return board[0]
    elif (row2):
        return board[3]
    elif (row3):
        return board[6]
        
    return

# Checking of Columns for Win
    
def check_columns():
    
     global game_running
     
     column1  =  board[0]  ==  board[3]  ==  board[6] != "_"
     column2  =  board[1]  ==  board[4]  ==  board[7] != "_"
     column3  =  board[2]  ==  board[5]  ==  board[8] != "_"
    
     if (column1 or column2 or column3):
        game_running = False
        
     if (column1):
        return board[0]
     elif (column2):
        return board[1]
     elif (column3):
        return board[3]
        
     return

# Checking of Diagonals for Win

def check_diagonals():
     global game_running
     diagonal1  =  board[0]  ==  board[4]  ==  board[8] != "_"
     diagonal2  =  board[6]  ==  board[4]  ==  board[2] != "_"
    
     if (diagonal1 or diagonal2):
        game_running = False
        
     if (diagonal1):
        return board[0]
     elif (diagonal2):
        return board[6]      

     return
    

# Checking of the Game is Tie or not
     
def check_tie():
    global game_running
    if "_" not in board:
        game_running = False
        
        return
    
game()