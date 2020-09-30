################################################################
###########               TIC-TAC-TOE                ###########
###########            by Miguel Pedraza             ###########
################################################################

# ------------GLOBAL VARIABLES-------------

# List that represents the board in which we play
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

# Game still going
playingGame = True

# Who won?
winner = None

# Whos next?
currentPlayer = "X"

# ------------END GLOBAL VARIABLES-------------

# ------------FUNCTIONS------------
# Funcion that prints the board
def showBoard():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])

# Function play 
def play():
    print("******************************************************************************************************************")
    print("*                                            WELCOME TO TIK-TAC-TOE                                              *")
    print("*                                              by Miguel Pedraza                                                 *")
    print("******************************************************************************************************************")
    print("")
    print("Instructions: Pick a position from 1-9 in order to place your X or O in the board. Have fun playing with a friend!")
    print("")
    # Call the function in order to display the initial board 
    showBoard()

    while playingGame:
        # Handle the first turn 
        handleTurn(currentPlayer)
        # Check weather somebody has won or tie
        checkIfGameOver()
        # Change player
        nextPlayer()

    # Game has ended
    if winner == "X" or winner == "O":
        print(winner + " won!")
    elif winner == None:
        print("Tie!")

# Function to handle turn choosing a number from 1-9
def handleTurn(player):
    print(player + " turn.")
    position = input("Choose a position from 1-9: ")

    valid = False
    while not valid: 
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Invalid input. Choose a position from 1-9: ") 

        # We subtract 1 because of index starts at 0
        position = int(position) - 1

        if board[position] == "-":
            valid = True
        else:
            print("You can't go there. Pick again")

    # Input where the user chose to
    board[position] = player
    # Show the pick
    showBoard()

# Function to verify if the game ended
def checkIfGameOver():
    checkIfWin()
    checkIfTie()

# Function to check if somebody won 
def checkIfWin():
    # Set up global variables
    global winner

    # Check rows
    rowWinner = checkRows()
    # Check columns
    columnWinner = checkColumns()
    # Check diagonal
    diagonalWinner = checkDiagonals()

    if rowWinner:
        winner = rowWinner
    elif columnWinner:
        winner = columnWinner
    elif diagonalWinner:
        winner = diagonalWinner
    else:
        winner = None
    return

# Function to check if a player won with a row
def checkRows():
    # Set up global variables
    global playingGame

    # Check if any row have the same value (excluding the dash from the beginning)
    row1 = board[0] == board[1] == board[2] != "-"
    row2 = board[3] == board[4] == board[5] != "-"
    row3 = board[6] == board[7] == board[8] != "-"
    # If theres a match we stop the game
    if row1 or row2 or row3:
        playingGame = False
    # Return the winner X or O
    if row1:
        return board[0]
    elif row2:
        return board[3]
    elif row3:
        return board[6]
    return
    
# Function to check if a player won with a column
def checkColumns():
    # Set up global variables
    global playingGame

    # Check if any row have the same value (excluding the dash from the beginning)
    column1 = board[0] == board[3] == board[6] != "-"
    column2 = board[1] == board[4] == board[7] != "-"
    column3 = board[2] == board[5] == board[8] != "-"
    # If theres a match we stop the game
    if column1 or column2 or column3:
        playingGame = False
    # Return the winner X or O
    if column1:
        return board[0]
    elif column2:
        return board[1]
    elif column3:
        return board[2]
    return

# Function to check if a player won with a diagonal
def checkDiagonals():
    # Set up global variables
    global playingGame

    # Check if any row have the same value (excluding the dash from the beginning)
    diagonal1 = board[0] == board[4] == board[8] != "-"
    diagonal2 = board[6] == board[4] == board[2] != "-"
    # If theres a match we stop the game
    if diagonal1 or diagonal2:
        playingGame = False
    # Return the winner X or O
    if diagonal1:
        return board[0]
    elif diagonal2:
        return board[6]
    return

# Function to check if the game tied 
def checkIfTie():
    # Global Variables
    global playingGame
    # Check if there are still dashes on the board if not then is a tie
    if "-" not in board:
        playingGame = False
    return

# Function to check player and change to the next one
def nextPlayer():
    # Global variables
    global currentPlayer
    # Check if it is x change to o and viceversa
    if currentPlayer == "X":
        currentPlayer = "O"
    elif currentPlayer == "O":
        currentPlayer = "X"
    return

# ------------END FUNCTIONS------------

# ------------START PROGRAM------------

# Start to play
play()