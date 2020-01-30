import random

class Nonogramm:
	def __init__(self, sizeX, sizeY):
		self.sizeX = sizeX
		self.sizeY = sizeY
		self.field = [[0 for x in range(sizeX)] for y in range(sizeY)]
		self.inputX = [[0 for x in range(sizeX)] for y in range(3)]
		self.inputX = [[1,1],[1],[4],[1],[2,1],[2,1]]
		self.inputY = [[0 for x in range(sizeY)] for y in range(3)]
		self.inputY = [[1,1,2],[1,2],[3],[4]]
		self.solved = 0
	
	def printNG(self):
		print("Testprint.")
	
	def printField(self):
		print("Current field:")
		for y in range(self.sizeY):
			print(self.field[y])
	
	def printInput(self):
		print("InputX")
		print(self.inputX)
		print("InputY")
		print(self.inputY)
	
	def solveRandom(self):
		for y in range(self.sizeY):
			for x in range(self.sizeX):
				self.field[y][x] = random.randint(0,1)
	
	def check(self):
		guard = 0
		
		horizontalSum = 0
		for y in range(self.sizeY):
			if sum(self.field[y]) == sum(self.inputY[y]):
				horizontalSum = horizontalSum + 1
		if horizontalSum == self.sizeY:
			guard = guard + 1
		
		verticalSum = 0
		for x in range(self.sizeX):
			sumField = 0
			for y in range(self.sizeY):
				sumField = sumField + self.field[y][x]
			if sumField == sum(self.inputX[x]):
				verticalSum = verticalSum + 1
				
			if verticalSum == self.sizeX:
				guard = guard + 1
		
		if guard == 2:
			return 1
		else:
			return 0
	

NG = Nonogramm(6,4)
NG.printInput()
while(NG.check() == 0):
	NG.solveRandom()
NG.printField()

input("Press ENTER to exit.")