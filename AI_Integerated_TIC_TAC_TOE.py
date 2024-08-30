def Board(board):
  print("Current State of the Board: \n\n")
  for i in range(0, 9):
    if ((i > 0) and (i % 3) == 0):
      print("\n");
    if (board[i] == 0):
      print("_ ", end = " ");
    if (board[i] == 1):
      print("O ", end = " ");
    if (board[i] == -1):
      print("X ", end = " ");
  print("\n\n");

def Player1Turn(board):
  pos = input("Enter X's position from [1...9]: ")
  pos = int(pos)
  if (board[pos - 1] != 0):
    print("Wrong Move!")
    exit(0)
  board[pos - 1] = -1;

def Player2Turn(board):
  pos = input("Enter O's position from [1...9]: ")
  pos = int(pos)
  if (board[pos - 1] != 0):
    print("Wrong Move!")
    exit(0)
  board[pos - 1] = 1;

def minmax(board, player):
  x = analyzeboard(board)
  if (x != 0):
    return (x * player)
  
  pos = -1
  value = -2
  for i in range(0, 9):
    if (board[i] == 0):
      board[i] = player
      score = -minmax(board, player * -1)
      board[i] = 0
      if (score > value):
        value = score
        pos = i
  if (pos == -1):
    return 0
  return value

def AI_Turn(board):
  pos = -1
  value = -2
  for i in range(0, 9):
    if (board[i] == 0):
      board[i] = 1
      score = -minmax(board, -1)
      board[i] = 0
      if (score > value):
        value = score
        pos = i
  board[pos] = 1

def analyzeboard(board):
  cb = [[0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]]
  for i in range(0, 8):
    if (board[cb[i][0]] != 0 and
        board[cb[i][0]] == board[cb[i][1]] and
        board[cb[i][0]] == board[cb[i][2]]):
      return board[cb[i][0]]  
  return 0  


def main():
  while True:
    print("AI Integrated TIC TAC TOE in Python")
    choice = input("Enter 1 for Single-Player, 2 for Multiplayer Game, or -1 to Quit: ")
    choice = int(choice)
    
    if choice == -1:
      print("Thanks for playing!")
      break
    
    board = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    
    if choice == 1:
      print("Computer: O vs. You: X")
      player = input("Enter 1 to play 1st Move or 2 to play 2nd Move: ")
      player = int(player)
      for i in range(0, 9):
        if analyzeboard(board) != 0:
          break
        if (i + player) % 2 == 0:
          AI_Turn(board)
        else:
          Board(board)
          Player1Turn(board)
    elif choice == 2:
      for i in range(0, 9):
        if analyzeboard(board) != 0:
          break
        if i % 2 == 0:
          Board(board)
          Player1Turn(board)
        else:
          Board(board)
          Player2Turn(board)
    
    x = analyzeboard(board)
    if x == 0:
      Board(board)
      print("Draw!")
    elif x == -1:
      Board(board)
      print("Player X Wins!")
    elif x == 1:
      Board(board)
      print("Player O Wins!")

main()
