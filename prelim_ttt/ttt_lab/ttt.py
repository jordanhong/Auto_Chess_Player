from tttlib import *
def valid_input(x):
   if type(x)==bool or x not in (str(x) for x in range (0, 9, 1)) :
      return False
   else:
      return True



T = genBoard()
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
   moveO = input("O move?")
   # check moveO for valid input
   # if valid and if T is unoccupied at moveO, set the appropriate
   # position of T via: T[int(moveO)] = 2
   while not (valid_input(moveO) and T[int(moveO)]==0):
      moveO = input("Invalid input, O move?")

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
