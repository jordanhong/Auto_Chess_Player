import random

class tree:
	def __init__(self, x):
		self.store=[x, []]

	def GetRootNode(self):
		return self.store[0]

	def AddSuccessor(self, x):
		self.store[1]=self.store[1]+[x]
		return True
	def GetSuccessors(self):
		return self.store[1]


	def Print_DepthFirst(self, c):
		x=self.store[0]
		#if x.change==[10, 17, 24]:
		print ("	"*c,x.change, x.val, x.stren)
		#	x.evaluateBoard(20)
		if (self.store[1]==[]):
			return True
		else:
			for x in self.store[1]:
				x.Print_DepthFirst(c+1)

	def Get_LevelOrder(self):

		x=queue()
		lin=[]
		x.enqueue(self)
		while(not x.empty()):
			r=x.dequeue() #dequeues out an actual tree
			ca=r.GetRootNode()
			#lin+=[(ca.change,  ca.val,  ca.stren)]
			lin+=[ca]
			for i in r.store[1]:
				x.enqueue(i)

			r=-1
			c=-1

		return lin

	








class queue:
	def __init__(self):
		self.store=[]
	def enqueue(self, x):
		self.store+=[x]
		return 0
	def dequeue(self):
		if (len(self.store)==0):
			return -1
		else:
	 		r=self.store[0]
	 		self.store=self.store[1:len(self.store)]
	 		return r


	def empty(self):
		if (len(self.store)==0):
			return True
		else:
	 		return False

class board():



	def __init__(self):
		self.numrow=8
		self.numcol=8
		self.store=[]
		self.default_config()
		self.stren="null" # stren is the direct ratings returned by the metic 
		self.val="null" # val stores the result of min max	
		self.change=["null", "null", "null"] # player, old loc, new loc


	def default_config(self):

		setup=[3, 1, 2, 5, 4, 2, 1, 3]
		w=10
		b=20


		self.store=[0]*self.numcol*self.numrow
		for r in range (0, self.numrow, 1):
			for c in range (0, self.numcol, 1):
				if r==0:
					self.store[r*self.numcol+c]=setup[c]+w
				elif r==7:
					self.store[r*self.numcol+c]=setup[c]+b

				elif r==1:
					self.store[r*self.numcol+c]=10
				elif r==6:
					self.store[r*self.numcol+c]=20


		return True



	def Getstore(self):
		print(self.store)



	def convert_to_display(self):
		display=list(self.store)
		odd=["___", "###", "___", "###", "___" ,"###", "___", "###"]
		even=["###", "___","###", "___","###", "___","###", "___"]
		for r in range (0, self.numrow, 1):
			for c in range (0, self.numcol, 1):


				index=r*self.numcol+c
				if (display[index]==0):
					if (r%2==0):
						display[index]=even[c]
					else:
						display[index]=odd[c]
				else:
					display[index]=self.returnPiece(index)

		return display


	def returnPiece(self, pos):
		offset=self.store[pos]//10
		val=self.store[pos]%10
		accum=""
		if offset==1:
			accum+="W"
		elif offset==2:
			accum+="B"

		else:
			return accum

		if val==0:
			accum+="Pa"
		elif val==1:
			accum+="Kn"
		elif val==2:
			accum+="Bi"
		elif val==3:
			accum+="Ro"
		elif val==4:
			accum+="Qn"
		elif val==5:
			accum+="Kg"
		return accum










	def printBoard(self):

		display=self.convert_to_display()
		print("\n---- BLACK SIDE ----\n")
		for r in range (self.numrow-1, -1, -1):
			print('%-3s  %-3s  %-3s  %-3s  %-3s  %-3s  %-3s  %-3s			%-3s  %-3s  %-3s  %-3s  %-3s  %-3s  %-3s  %-3s' % (display[r*self.numcol+7], display[r*self.numcol+6], display[r*self.numcol+5], display[r*self.numcol+4], display[r*self.numcol+3], display[r*self.numcol+2], display[r*self.numcol+1], display[r*self.numcol+0], r*self.numcol+7, r*self.numcol+6, r*self.numcol+5, r*self.numcol+4, r*self.numcol+3, r*self.numcol+2, r*self.numcol+1, r*self.numcol+0))

		print("\n---- WHITE SIDE ----\n")

		return True
	

	def setPiece(self, c, n):
	#	if type(c)!=int:
	#		print ("Int not passed in")
	#		return False
	#
	#	if type(n)!=int:
	#		print ("Int not passed in")
	#		return False
		self.store[n]=self.store[c]
		self.store[c]=0
		return True

	def GetPlayerPositions(self, player):
		board=self.store
		pos=[]
		for i in range (0, len(board), 1):
			if(board[i]//10)==(player//10):
				pos+=[i]

		return pos


	def IsOnBoard(self, pos):
		if (pos>=0)and (pos<=63):
			return True
		else:
			return False


	def incr(self, pos, inc, lim):  # lim is the boundary condition
		legalpos=[]
		r=pos
		while ( self.IsOnBoard(r+inc)):
			if (r%self.numcol==lim ):
				#print("reached boundary at ", r)
				break

			# checks if is blocked by self(compared to current pos), if yes, break before adding in 
			if self.selfblock(pos, r+inc):
			#	print("blocked by self piece, terminated before moving: ", r+inc)
				break
			r+=inc
			legalpos+=[r]
			# check if blocked by opponent, if yes, then break after adding in, i.e. captured the opponent
			if self.oppoblock(pos, r):
			#	print("blocked by opponent at: , taken down and stopped ", r)
				break


			# check if arrived at border, set by lim, using the % to see column
			# do not need to check rows because row do not roll over. If row is exceeded, automatically out of boundary
			if (r%self.numcol==lim ):
			#	print("reached boundary at ", r)
				break
		#print("legal pos for this direction: ", legalpos)
		return legalpos


	def GetBishopMoves(self, pos):
		legalpos=[]
		r=pos

		#up right
		legalpos+=self.incr(pos, 7, 0)

		#down left
		legalpos+=self.incr(pos, -7, 7)


		#up left
		legalpos+=self.incr(pos, 9, 7)

		#down right
		legalpos+=self.incr(pos, -9, 0)

		return legalpos


	def GetRookMoves(self,pos):
		legalpos=[]
		#up
		legalpos+=self.incr(pos, 8, 8)
		#down
		legalpos+=self.incr(pos, -8, 8)
		#left
		legalpos+=self.incr(pos, 1, 7)
		#right
		legalpos+=self.incr(pos, -1, 0)

		return legalpos


	def GetQueenMoves(self, pos):
		return self.GetRookMoves(pos) + self.GetBishopMoves(pos)


	def check2d(self, r, c):
		if (r<self.numrow and c<self.numcol)and(r>=0 and c>=0):
			return True
		else:
			return False


	def GetKingMoves(self, pos):
		legalpos=[]
		r=pos//self.numcol
		c=pos%self.numcol

		for i in range(r-1, r+2, 1):
			for j in range(c-1, c+2, 1):
				if not (i==r and j==c) and self.check2d(i, j):
					index=i*self.numcol+j
					if self.IsOnBoard(index) and not self.selfblock(pos, index):
						legalpos+=[index]

		return legalpos


	def GetKnightMoves(self, pos):
		legalpos=[]
		r=pos//self.numcol
		c=pos%self.numcol
		
		for i in range (r-2, r+3, 4):
			for j in range (c-1, c+2, 2):
				if self.check2d(i, j):
					index=i*self.numcol+j
					if not self.selfblock(pos, index):
						legalpos+=[index]


		for i in range (r-1, r+2, 2):
			for j in range (c-2, c+3, 4):
				if self.check2d(i, j):
					index=i*self.numcol+j
					if not self.selfblock(pos, index):
						legalpos+=[index]

		return legalpos
		

	def GetPawnMoves(self, pos):
		legalpos=[]
		r=pos//self.numcol
		c=pos%self.numcol
		player=self.store[pos]//10
		incr=0
		if player==1:
			incr=1
		else:
			incr=-1
		

		if self.check2d(r+incr, c): #moving ahead wo capturing
			index=(r+incr)*self.numcol+c
			if not self.selfblock(pos, index) and not self.oppoblock(pos, index): # not blocked by either party
				legalpos+=[index]
		

		if self.check2d(r+incr, c-1): #capturing upper right
			#insert check opponent
			index=(r+incr)*self.numcol+c-1
			if self.oppoblock(pos, index):
				legalpos+=[index]

		if self.check2d(r+incr, c+1): #capturing upper left
			#insert check opponent
			index=(r+incr)*self.numcol+c+1
			if self.oppoblock(pos, index):
				legalpos+=[index]


		return legalpos



	#returns True of the next position is self piece, False if opponent piece or vacant
	def isself(self, c, n): #c for current position, and n for next position
		if (self.store[c]//10==self.store[n]//10):
			return True
		else:
			return False



	def selfblock(self, c, n):
		if self.store[n]==0: # if vacant
			return False

		else:
			return self.isself(c, n)
	

	def oppoblock(self, c, n):
		if self.store[n]==0:
			return False
		else:
			return not self.isself(c, n)



	# passes in the index of the board (position)
	# returns a list of all legal positions that the piece in the given position can take
	
	def GetPieceLegalMoves(self, pos):
		c=self.store[pos]
		if c==0: 
			return False # no pieces there, invalid
		val=c%10 #calc the actual val, wo the offset
	
		if val==0:#pawn
			return self.GetPawnMoves(pos)
		elif val==1: #knight
			return self.GetKnightMoves(pos)
		elif val==2:
			return self.GetBishopMoves(pos)
		elif val==3:
			return self.GetRookMoves(pos)
		elif val==4:
			return self.GetQueenMoves(pos)
		elif val==5:
			return self.GetKingMoves(pos)

		else:
			return False
			
			

	def oppo(self, player):
		if player//10==1:
			return 20
		elif player//10==2:
			return 10

		else:
			return 0


	def IsPositionUnderThreat(self, pos, player):
		opponent=self.oppo(player)
		if opponent==0:
			return False  # error checks if opponent is defined the game
		oppopos=self.GetPlayerPositions(opponent)
		temp=[]
		for x in oppopos:
			temp=self.GetPieceLegalMoves(x)
			if pos in temp:
				return True

		return False


	def checkstate(self):

		if 15 not in self.store:
			return 2  #black wins

		elif 25 not in self.store:
			return 1 #white wins

		else:
			return 0


	def evaluateBoard(self, player):
		strength=[10.0, 30.0, 30.0, 50.0, 90.0, 900.0]
		# receives 10 for white and 20 for black
		# returns the board value
		player//=10
		temp=0
		for x in self.store:
			if (x!=0):
				p=x//10
				if (p==player):
					#if (self.change==[10, 17, 24]):
					#	print ("added in", strength[x%10])
					temp+=strength[x%10]
				else:
					#if(self.change==[10, 17, 24]):
					#	print ("subtracted: ", strength[x%10])
					temp-=strength[x%10]
		self.stren=temp
		#if (self.change==[10, 17, 24]):
		#	self.printBoard()
		#	print ("eval is ", temp)
		return temp


	def checkmate(self, player):
		hasKing=self.findKing(player)
		if (kasKing==-1):
			return False
		r=self.IsPositionUnderThreat(king, player)
		return r


	def findKing(self, player):
		pos=self.GetplayerPositions(player)
		#identify King
		king=-1
		for c in pos:
			if (self.store[c]%10 ==5):
				king=c
				break
		return king

		


	def createTree(self, original, player, btree, depth):
		if (depth!=0) and (self.findKing!=-1):
			pos=self.GetPlayerPositions(player)
			for c in pos:
				x= self.GetPieceLegalMoves(c)
				for e in x:
					# for each legal move, instantiate a new board
					new=board()
					new.store=list(self.store)
					# stick the legal moves
					new.setPiece(c, e)
					new.change=[player, c, e]
					if depth==1 or new.findKing==-1:
						new.evaluateBoard(original)
						new.val=new.stren

					#create a new tree
					newtree=tree(new)
					new.createTree(original, self.oppo(player), newtree, depth-1)
					

					btree.AddSuccessor(newtree)
		
				 

	
			# insert the minMax function here
			children=btree.GetSuccessors()
			temp=children[0].GetRootNode().val
			for child in children:
			# Max
				if (original==player):
					if child.GetRootNode().val>temp:
						temp=child.GetRootNode().val
			#Min
				else:
					if child.GetRootNode().val<temp:
						temp=child.GetRootNode().val
			
			
			btree.GetRootNode().val=temp
					



		return True


	def chessPlayer(self, player):
		# passes in a player and returns a move 
		# checks if king is checked 
			
		chess_tree=tree(self)
		self.createTree(player, player,chess_tree,4)
		#get the results for min max
		rval=self.val
		r=-1
		children=chess_tree.GetSuccessors()
		for child in children:
			if child.GetRootNode().val==rval:
				r=child.GetRootNode().change		
				break				



		#print("level order", chess_tree.Get_LevelOrder())
		print ("depth first")
		chess_tree.Print_DepthFirst(0)
		print( "Computer moved from: %d to: %d" %(r[1], r[2]))
		return r
		
			
			
def select(inputlist, key):
	accum=[]
	for x in inputlist:
		if x[1]==key:
			accum+=[x]
	if accum==[]:
		return -1000

	return accum[ random.randint (0, len(accum)-1)][0]			
						
def chessPlayer(b, player):
	try:
		chess_board=board()
		chess_board.store=b

		chess_tree=tree(chess_board)
		chess_board.createTree(player, player, chess_tree, 3)
		rval=chess_board.val
		r=-1
		children=chess_tree.GetSuccessors()

		accum=[]
		for child in children:
			accum+=[[ [child.GetRootNode().change[1], child.GetRootNode().change[2]], child.GetRootNode().val]]


		#for x in accum:
		#	if x[1]==rval:
		#		r=x[0]
		#		break

		r=select(accum, rval)

		level_traverse=chess_tree.Get_LevelOrder()	
		#print([True, r, accum, level_traverse])
		return [True, r, accum, level_traverse]
	except:
		return [False, [], [[], 0.0], -1]




												 	

