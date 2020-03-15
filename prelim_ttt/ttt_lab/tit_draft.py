## Tic TaT Toe
board=[2, 1, 2, 1, 2, 2, 2, 1, 1, 0]
def genBoard():
   board=[]
   board_len=9
   i=0
   while i<board_len:
      board=board+[0]
      i=i+1
   return board


def printBoard(T):
   i=0
   display=[]
   board_len=9
   if not len(T)== board_len:
      return False
   while i<board_len:
      if T[i]==0:
         display=display+[str(i)]
      elif T[i]==1:
         display=display+["X"]
      elif T[i]==2:
         display=display+["O"]
      else:
         return False
      i=i+1    
   i=0
   while i<board_len:
      print (" "+display[i]+ " | "+display[i+1]+" | "+display[i+2])
      if i !=6:
         print ("---|---|---")
      i=i+3
   return True

def analyzeBoard(T):
   board_len=9
   if not len(T)==board_len:
      return -1
   for c in T:
     if not (c==0 or c==1 or c==2):
         return -1
   winnings=[[0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 4, 8], [2, 4, 6]]
   for c in winnings:
      if T[c[0]]==T[c[1]]==T[c[2]]:
         return T[c[0]]
      elif 0 in T:
         return 0
   return 3
print (analyzeBoard(board))
#print (printBoard(board))
#print (printBoard(genBoard()))
