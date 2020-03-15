
class tree:
	def __init__(self, x):
		self.store=[x, []]
	

	def AddSuccessor(self, x):
		self.store[1]=self.store[1]+[x]
		return True


	def Print_DepthFirst(self, c):
		print (" "*c+str(self.store[0]))

		if (self.store[1]==[]):
			return True
		else:
			c+=1
			for x in self.store[1]:
				x.Print_DepthFirst(c)

	def Get_LevelOrder(self):
		x=queue()
		lin=[]
		x.enqueue(self)
		while(not x.empty()):
			r=x.dequeue()
			lin+=[r.store[0]]
			for i in r.store[1]:
				x.enqueue(i)
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
	
		












