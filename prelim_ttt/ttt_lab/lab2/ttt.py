from tttlib import *
def valid_input(x):
   if type(x)==bool or x not in (str(x) for x in range (0, 9, 1)) :
      return False
   else:
      return True

def player_action(T, player_list, player, move):
   T[int(move)]=player
   state = analyzeBoard(T)

   # check if state says X won and act accordingly and break

   if state==player:
      printBoard(T)
      print (player_list[player-1], " won")
      return False
 # check if state says draw and act accordingly and break
   elif state==3:
      print("Draw")
      return False
   return True


def humaninput(T, player_list, player):
   move = input(player_list[player-1]+ " move?")
   while not (valid_input(move) and T[int(move)]==0):
      move=input("invalid input."+ player_list[player-1]+ " move?")
   return move

def ask_order():
   player_ord=input("Enter 1 to go first as 'X', otherwise enter 2 to go second as 'O'.")
   while player_ord not in ("1", "2"):
       player_ord=input("invalid input. Enter 1 to go first as 'X', otherwise enter 2 to go second as 'O'.")
   return int (player_ord)


def main():
   player_list=["X", "O"]
   T = genBoard()
   order=ask_order()
   printBoard(T)
   while True:
      if order==1:
         if not player_action(T, player_list, 1, humaninput(T, player_list, 1)):
            break
         computer=player_action(T, player_list, 2,AI(T, 2) )
         print()
         printBoard(T)
         print()
         if not computer:
            break
      elif order==2:
         computer=player_action(T, player_list, 1,AI(T, 1) )
         print  ()
         printBoard(T)
         print()
         if not computer:
            break
         if not player_action(T, player_list, 2, humaninput(T, player_list, 2)):
            break
   return True
main()


'''
while True:
   printBoard(T)
   print ()
   moveX = input("X move?")
   # check moveX for valid input
   # if valid and if T is unoccupied at moveX, set the appropriate
   # position of T via: T[int(moveX)] = 1
   while not (valid_input(moveX) and T[int(moveX)]==0):
      moveX=input("invalid input, X move?")
   T[int(moveX)]=1


   state = analyzeBoard(T)

   # check if state says X won and act accordingly and break

   if state==1:
      printBoard(T)
      print ("X won")
      break
 # check if state says draw and act accordingly and break
   elif state==3:
      print("Draw")
      break

   printBoard(T)
   print ()
   moveO = AI(T, 2)
   # check moveO for valid input
   # if valid and if T is unoccupied at moveO, set the appropriate
   # position of T via: T[int(moveO)] = 2

   T[int(moveO)]=2
   state = analyzeBoard(T)
   
   # check if state says O won and act accordingly and break
   # check if state says draw and act accordingly and break
   if state==2:
      printBoard(T) 
      print("O won")
      break
   elif state==3:
      printBoard(T)
      print("Draw")
      break
'''
