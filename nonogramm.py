import random
import time

class Nonogramm:
    def __init__(self, size, inputInfo):
        self.sizeX = size[0]
        self.sizeY = size[1]
        self.field = [[0 for x in range(self.sizeX)] for y in range(self.sizeY)]
        #self.inputInfoX = [[0 for x in range(self.sizeX)] for y in range(3)]
        self.inputInfoX = inputInfo[0]
        #self.inputInfoX = [[1,1],[1],[4],[1],[2,1],[2,1]]
        #self.inputInfoX = [[1],[2],[1]]
        #self.inputInfoX = [[1],[1]]
        #self.inputInfoX = [[1],[2],[2],[1,2]]
        #self.inputInfoX = [[1],[1],[1],[1]]
        #self.inputInfoX = [[1,1],[1],[3,1],[2,2],[1,1]]
        #self.inputInfoY = [[0 for x in range(self.sizeY)] for y in range(3)]
        self.inputInfoY = inputInfo[1]
        #self.inputInfoY = [[1,1,2],[1,2],[3],[4]]
        #self.inputInfoY = [[1],[2],[1]]
        #self.inputInfoY = [[1],[1]]
        #self.inputInfoY = [[1,1],[3],[2],[1]]
        #self.inputInfoY = [[4],[0],[0],[0]]
        #self.inputInfoY = [[1,2],[3],[1,1],[1,1],[3]]
        #self.solved = 0
    
    def printNG(self):
        print("Testprint.")
    
    def printField(self):
        for y in range(self.sizeY):
            print(self.field[y])
    
    def printinputInfo(self):
        print("inputInfoX")
        print(self.inputInfoX)
        print("inputInfoY")
        print(self.inputInfoY)
    
    def solveRandom(self):
        # 0.535ms for 2x2 in average
        # 5.26ms for 3x3 in average
        # 3.86s for 4x4 in average
        # 547s for 6x4 measured once
        for y in range(self.sizeY):
            for x in range(self.sizeX):
                self.field[y][x] = random.randint(0,1)
    
    def solveRandomBetter(self):
        # ms for 2x2 in average
        # ms for 3x3 in average
        # s for 4x4 in average
        # s for 6x4 measured once
        for y in range(self.sizeY):
            for x in range(self.sizeX):
                self.field[y][x] = int(round(random.randint(0,1) + ((sum(self.inputInfoY[y]) / self.sizeX) - 0.5)))
    
    def check(self):
        guard = 0
        
        horizontalSum = 0
        for y in range(self.sizeY):
            if sum(self.field[y]) == sum(self.inputInfoY[y]):
                horizontalSum += 1
        if horizontalSum == self.sizeY:
            guard += 1
        
        verticalSum = 0
        for x in range(self.sizeX):
            sumField = 0
            for y in range(self.sizeY):
                sumField = sumField + self.field[y][x]
            if sumField == sum(self.inputInfoX[x]):
                verticalSum += 1
            
        if verticalSum == self.sizeX:
            guard += 1
        
        horizontalSpacing = 0
        for y in range(self.sizeY):
            foundinputInfoY = []
            foundinputInfoY.append(0)
            
            for x in range(self.sizeX):
                if self.field[y][x] == 1:
                    if x == 0:
                        foundinputInfoY[0] += 1
                    else:
                        if self.field[y][x - 1] == 0:
                            if foundinputInfoY[0] != 0:
                                foundinputInfoY.append(0)
                        foundinputInfoY[len(foundinputInfoY) - 1] += 1
            if foundinputInfoY == self.inputInfoY[y]:
                horizontalSpacing += 1
        if horizontalSpacing == self.sizeY:
            guard += 1
        
        verticalSpacing = 0
        for x in range(self.sizeX):
            foundinputInfoX = []
            foundinputInfoX.append(0)
            
            for y in range(self.sizeY):
                if self.field[y][x] == 1:
                    if y == 0:
                        foundinputInfoX[0] += 1
                    else:
                        if self.field[y - 1][x] == 0:
                            if foundinputInfoX[0] != 0:
                                foundinputInfoX.append(0)
                        foundinputInfoX[len(foundinputInfoX) - 1] += 1
            if foundinputInfoX == self.inputInfoX[x]:
                verticalSpacing += 1
        if verticalSpacing == self.sizeX:
            guard += 1
        
        if guard == 4:
            return 1
        else:
            return 0

print("Starting session.")

gameNumber = 10
startTime = time.time()


inputInfo = [[[1], [2], [2], [1, 2]],
         [[1, 1],
          [3],
          [2],
          [1]
         ]
        ]

size = [len(inputInfo[0]), len(inputInfo[1])]
print("\nInput information:")
print(inputInfo)
print("\nSize:")
print(size)

for x in range(gameNumber):
    NG = Nonogramm(size, inputInfo)
    
    while(NG.check() == 0):
        NG.solveRandomBetter()
    
    print("\nSolution:")
    NG.printField()

print("\nAverage time:", (time.time() - startTime) / gameNumber, "seconds")



input("\nPress ENTER to exit.")