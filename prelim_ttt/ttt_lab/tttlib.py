
import random
def genBoard():
   board=[]
   board_len=9
   for i in range(0,board_len,1):
      board=board+[0]
   return board

def printBoard(T):

   display=[]
   board_len=9
   if not type(T)==list:
      return False
   if (not len(T)== board_len):
      return False
   for i in range(0,board_len,1):
      if not (type(T[i])==int):
        return False
      if T[i]==0:
         display=display+[str(i)]
      elif T[i]==1:
         display=display+["X"]
      elif T[i]==2:
         display=display+["O"]
      else:
         return False

   for i in range (0,board_len,3):
      print (" "+display[i]+ " | "+display[i+1]+" | "+display[i+2])
      if i !=6:
         print ("---|---|---")

   return True

def analyzeBoard(T):
   board_len=9
   if not type(T)==list:
      return -1
   if not len(T)==board_len :
      return -1
   for c in T:
      if not (c==0 or c==1 or c==2) or not (type(c)==int):
         return -1
   count=[0,0]
   for x in T:
      if x==1:
         count[0]+=1
      elif x==2:
         count[1]+=1
   if not (count[0]-count[1]==1 or count[0]-count[1]==0 or count[0]-count[1]==-1):
      return -1
      
   winnings=[[0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 4, 8], [2, 4, 6]]
   winners=[]
   for c in winnings:
      if T[c[0]]==T[c[1]]==T[c[2]] and not (T[c[0]]==0):
         winners+=[T[c[0]]]
   if not len(winners)<=1:
      return -1
   elif len(winners)==1:
      return winners[0]
   if 0 in T:
      return 0
   else:
      return 3

def oppo(player):
   if player==1:
      return 2
   elif player==2:
      return 1
   else:
      return -1

def testwin(T, player):
   board= list(T)
   for i in range (len(board)):
      if board[i]==0:
         board[i]=player
         if analyzeBoard(board)==player:
            return i
         else:
            board[i]=0
   return -1

def genNonloser(T, player):
   return testwin( T, oppo(player))

def genWinningMove(T, player):
   return testwin(T, player)

def open_space(T):
   ava=[]
   for i in range (0, len(T), 1):
      if T[i]==0:
         ava+=[i]
   if len(ava)==0:
      return -1
def genRandomMove(T, player):
   ava=open_space(T)
   if ava==-1:
      return -1
   else:
      ran_move=ava[random.randint(0, len(ava)-1)]
   return ran_move 

def genOpenMove(T, player):
   ava=open_space(T)
   if ava==-1:
      return -1
   else:
      return ava[0]
  
