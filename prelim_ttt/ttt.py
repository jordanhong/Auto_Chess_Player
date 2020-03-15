from tttlib import *
def valid_input(x):
   if type(x)==bool or x not in (str(x) for x in range (0, 9, 1)) :
      return False
   else:
      return True

def player_action(T, player_list, player, move):
   T.store[int(move)]=player
   state = T.analyzeBoard()

   # check if state says X won and act accordingly and break
   if state==player:
      T.printBoard()
      print (player_list[player-1], " won")
      return False
 # check if state says draw and act accordingly and break
   elif state==3:
      print("Draw")
      return False
   return True


def humaninput(T, player_list, player):
   move = input(player_list[player-1]+ " move?")
   while not (valid_input(move) and T.store[int(move)]==0):
      move=input("invalid input."+ player_list[player-1]+ " move?")
   return move

def ask_order():
   player_ord=input("Enter 1 to go first as 'X', otherwise enter 2 to go second as 'O'.")
   while player_ord not in ("1", "2"):
       player_ord=input("invalid input. Enter 1 to go first as 'X', otherwise enter 2 to go second as 'O'.")
   return int (player_ord)


def main():
   player_list=["X", "O"]
   T = board()
   order=ask_order()
   T.printBoard()
   while True:
      if order==1:
         if not player_action(T, player_list, 1, humaninput(T, player_list, 1)):
            break
         computer=player_action(T, player_list, 2,T.computer( 2) )
         print()
         T.printBoard()
         print()
         if not computer:
            break
      elif order==2:
         computer=player_action(T, player_list, 1,T.computer(1) )
         print  ()
         T.printBoard()
         print()
         if not computer:
            break
         if not player_action(T, player_list, 2, humaninput(T, player_list, 2)):
            break
   return True
main()


