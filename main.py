##Tic Tac Toe
#Name: Ayden Bradley
#Date: Feb. 10th 2021
B = [' ']*7 + ['X'], ['O'], ['X']

theBoard = [' ']*10
#1. (Var) Setup the empty board as a list
#theBoard = {'7': ' ' , '8': ' ' , '9': ' ' ,           '4': ' ' , '5': ' ' , '6': ' ' ,            '1': ' ' , '2': ' ' , '3': ' ' }

#2. (fun) Print the board.
#in: a 10 item list (either x, o or ' ')
#do: print a graphic for the board
#out: none

def printBoard(board):
    print(board[7] + '|' + board[8] + '|' + board[9])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[1] + '|' + board[2] + '|' + board[3])
#3a. (fun) Determine if player is X or O
player1 = ''
player2 = ''

#in: None
#do: get user choice, assign X/O to player1 and 2
#out: None

def chooseLetter():
  global player1
  global player2
  letter = input("Which player would you like to be? X or O? ")
  if letter == 'X':
    player1 = "X"
    player2 = "O"
  else:
    player1 = "O"
    player2 = "X"




#3b. (fun) Choose starting player 1 or 2





#4. (fun) Get player move
#in: board as list, player as X or O
#do: get user choice (1-9),
#    check if the space is empty,
#    update the board with the X or O at the user location
#out: none

def playerMove(board, player):
    turn = int(input("Player " + player + ", what move would you like to make? Choose a number 1 through 9. "))
    print(" ")
    while board[turn] != ' ':
      print(" ")
      printBoard(theBoard)
      turn = input("That spot is already taken, choose a different spot. ")
      
    board[turn] = player
    printBoard(theBoard)
      
       


    




#5. (fun) Check Winner
#in: board as list, player as X or O
#do: check all possible win scenarios
#out: True for win, False otherwise
    
def checkWin(board, player):
  if board[1] == player and board[2] == player and board[3] == player:
    printBoard(theBoard)
    return True
  elif board[4] == player and board[5] == player and board[6] == player:
    printBoard(theBoard)
    return True
  elif board[7] == player and board[8] == player and board[9] == player:
    printBoard(theBoard)
    return True
  elif board[7] == player and board[4] == player and board[1] == player:
    printBoard(theBoard)
    return True
  elif board[8] == player and board[5] == player and board[2] == player:
    printBoard(theBoard)
    return True
  elif board[9] == player and board[6] == player and board[3] == player:
    printBoard(theBoard)
    return True
  elif board[7] == player and board[5] == player and board[3] == player:
    printBoard(theBoard)
    return True
  elif board[9] == player and board[5] == player and board[1] == player:
    printBoard(theBoard)
    return True
  else: return False


#6. (fun) Check if board is full
#Because there are 10 list items for 9 spots,
#the first item theBoard[0] will always be ' '
#in: board as list
#do: count number of empty spaces, if there is no more spaces
#out: return True if board is full, False otherwise

def checkFull(board):
    if board.count(' ') == 1:
      return True
    else:
      return False



#7. Main function

def main():
  print("Welcome to Tic Tac Toe!")
  print(" ")
  print("To win the game, get three of your own letter in a row on the board diagonally, horizontally, or vertically.")
  chooseLetter()

  while checkFull(theBoard) != True:
    playerMove(theBoard, player1)
    print(" ")
    if checkWin(theBoard, player1) == True:
      print("Player 1 Wins!")
      break
    if checkFull(theBoard) == True:
      print("Board is full, it's a draw.")
      break
    
    playerMove(theBoard, player2)
    print(" ")
    checkWin(theBoard, player2)
    checkFull(theBoard)
    if checkWin(theBoard, player2) == True:
      print("Player 2  Wins!")
      break
    if checkFull(theBoard) == True:
      print("Board is full, it's a draw.")
      break

main()

  
    
    

    #game play
    #get player letter choice
    
    #while board is not full
    ###first player move
        #player chooses move
        #print board
        #check win
        #check board full

    ###second player move
        #player chooses move
        #print baord
        #check win
    
    


