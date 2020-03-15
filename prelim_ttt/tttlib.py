from tree import *
import random


class board():
	def __init__(self):
		self.store=[];
		self.player=["", "X", "O"];
		self.state=0;
		self.val=0;
		self.length=9;
		for i in range (0, self.length, 1):
			self.store+=[0];
	

	def printBoard(self):

		display=[]
		if not type(self.store)==list:
			return False
		if (not len(self.store)== self.length):
			return False

		for i in range(0,self.length,1):
			if not (type(self.store[i])==int):
				return False



			if self.store[i]==0:
				display=display+[str(i)]
			elif self.store[i]==1:
				display=display+["X"]
			elif self.store[i]==2:
				display=display+["O"]
			else:
				return False

		for i in range (0,self.length,3):
			print (" "+display[i]+ " | "+display[i+1]+" | "+display[i+2])
			if i !=6:
				print ("---|---|---")


		return True

	def analyzeBoard(self):
		self.length=9
		if not type(self.store)==list:
			self.state= -1
			return self.state
		if not len(self.store)==self.length :
			self.state =-1
			return self.state
		for c in self.store:
			if not (c==0 or c==1 or c==2) or not (type(c)==int):
				self.state= -1
				return self.state


		winnings=[[0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 4, 8], [2, 4, 6]]
		winners=[]
		for c in winnings:
			if self.store[c[0]]==self.store[c[1]]==self.store[c[2]] and not (self.store[c[0]]==0):
				winners+=[self.store[c[0]]]
		if not len(winners)<=1:
			self.state= -1
			return self.state
		elif len(winners)==1:
			self.state= winners[0]
			return self.state
		elif 0 in self.store:
			self.state=0
			return self.state
		else:
			self.state=3
			return self.state
	

	def genWinningMove(self, player):
		return self.testwin(player)

	def genNonLoser(self, player):
		return self.testwin(self.oppo(player))


	def testwin(self, player):
		newboard=board()
		newboard.store=list(self.store)
		for i in range (len(newboard.store)):
			if newboard.store[i]==0:
				newboard.store[i]=player
				r=newboard.analyzeBoard()
				if r==player:
					return i;
				else:
					newboard.store[i]=0
		return -1


	def oppo(self, player):
		if player==1:
			return 2
		elif player==2:
			return 1
		else:
			return -1

	
	def genOpenMove(self):
		ava=self.open_space()
		if ava==-1:
			return -1

		else:
			return ava[0]

	def genRandomMove(self):
		ava=self.open_space()
		if ava==-1:
			return -1
		else:
			move=ava[random.randint(0, len(ava)-1)]
		return move 



	def open_space(self):
		ava=[]
		for i in range(0, len(self.store), 1):
			if self.store[i]==0:
				ava+=[i]

		if len(ava)==0:
			return -1

		return ava







	def lookup(self, player, btree, depth):
		if self.genWinningMove(player)!=-1:
			newboard=board()
			newboard.store=list(self.store)
			newboard.store[newboard.genWinningMove(player)]=player
			newboard.analyzeBoard()
			btree.AddSuccessor(tree(newboard))
			return True

		elif self.genNonLoser(player)!=-1:
			newboard=board()
			newboard.store=list(self.store)
			newboard.store[newboard.genNonLoser(player)]=player
			newboard.analyzeBoard()
			btree.AddSuccessor(tree(newboard))
			return True



		elif depth!=0:

			for i in range (0, self.length, 1):
				if self.store[i]==0:
					newboard=board()
					newboard.store=list(self.store)
					newboard.store[i]=player
					newboard.analyzeBoard()
					newtree=tree(newboard)
					self.lookup(self.oppo(player), newtree, depth-1)
					btree.AddSuccessor(newtree)

		return True




	def computer(self, player):
		if self.genWinningMove(player)!=-1:
			return self.genWinningMove(player)
		elif self.genNonLoser(player)!=-1:
			return self.genNonLoser(player)


		else:
			sim=tree(self)
			self.lookup(player, sim, 4)
			self.eval(sim,4) #depth of 4
			r=self.select_move(sim)
			return r

 
			
	
	def select_move(self, tree):
		
		ava=[]
		ava=self.open_space()
		temp=0
		for i in range (1, len(ava), 1):
			if  (tree.store)[1][temp].store[0].val< (tree.store)[1][i].store[0].val:
				temp=i
		return ava[i]
			





	def eval(self, tree, depth):
		if tree.store[1]==[]: #no successors
			tree.store[0].val=tree.store[0].state # assign the value as the state 
			return True

 
		

		if depth==1:
			temp=((tree.store[1])[0].store)[0].state #memo: change state in analyzeBoard

			for x in tree.store[1]:
				if x.store[0].state< temp:
					temp=x.store[0].state

		else:
			for x in tree.store[1]:
				self.eval(x, depth-1)


			temp=((tree.store[1])[0].store)[0].val #memo: change state in analyzeBoard

			for x in tree.store[1]:
				#if depth%2==0: #max
				if x.store[0].val>temp:
					temp=x.store[0].val
				#else:
				#	if x.store[0].val<temp:
				#		temp=x.store[0].val
	

		tree.store[0].val=temp
		return True


							
