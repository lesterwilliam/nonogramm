import random
import time

class Nonogramm:
    def __init__(self, size, inputInfo):
        self.sizeX = size[0]
        self.sizeY = size[1]
        self.inputInfoX = inputInfo[0]
        self.inputInfoY = inputInfo[1]
        self.field = [[0 for x in range(self.sizeX)] for y in range(self.sizeY)]
        self.fieldFound = [[0 for x in range(self.sizeX)] for y in range(self.sizeY)]
        # 0: unknown
        # 1: full
        # 2: empty

    def clear(self):
        self.field = [[0 for x in range(self.sizeX)] for y in range(self.sizeY)]
        self.fieldFound = [[0 for x in range(self.sizeX)] for y in range(self.sizeY)]

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

    def findBeginning(self):
        for y in range(self.sizeY):
            if sum(self.inputInfoY[y]) + len(self.inputInfoY[y]) - 1 == self.sizeX:
                tempInputInfoY = []
                tempInputInfoY2 = []
                for item in range(len(self.inputInfoY[y])):
                    tempInputInfoY.append(self.inputInfoY[y][item])
                    if item != (len(self.inputInfoY[y]) - 1):
                        tempInputInfoY.append(0)
                for item in tempInputInfoY:
                    if item != 0:
                        for amounthOfOnes in range(item):
                            tempInputInfoY2.append(1)
                    else:
                        tempInputInfoY2.append(0)

                self.fieldFound[y] = tempInputInfoY2
            #self.field[y] = self.fieldFound[y]

        for x in range(self.sizeX):
            if sum(self.inputInfoX[x]) + len(self.inputInfoX[x]) - 1 == self.sizeY:
                tempInputInfoX = []
                tempInputInfoX2 = []
                for item in range(len(self.inputInfoX[x])):
                    tempInputInfoX.append(self.inputInfoX[x][item])
                    if item != (len(self.inputInfoX[x]) - 1):
                        tempInputInfoX.append(0)
                for item in tempInputInfoX:
                    if item != 0:
                        for amounthOfOnes in range(item):
                            tempInputInfoX2.append(1)
                    else:
                        tempInputInfoX2.append(0)

                for y in range(self.sizeY):
                    if tempInputInfoX2[y] == 1:
                        self.fieldFound[y][x] = tempInputInfoX2[y]
        self.field = self.fieldFound

    def fillRandom(self):
        # before adding findBeginning
            # 0.535ms for 2x2 in average
            # 5.26ms for 3x3 in average
            # 3.86s for 4x4 in average
            # 547s for 6x4 measured once
        # after adding findBeginning
            # 100ms for 4x4 in nAverage

        for y in range(self.sizeY):
            for x in range(self.sizeX):
                if self.fieldFound[y][x] == 0:
                    self.field[y][x] = random.randint(0,1)

    def solveRandom(self):
        while(self.check() == 0):
            self.clear()
            self.findBeginning()
            self.fillRandom()

    def fillRandomBetter(self):
        # ms for 2x2 in average
        # ms for 3x3 in average
        # s for 4x4 in average
        # s for 6x4 measured once
        for y in range(self.sizeY):
            for x in range(self.sizeX):
                self.field[y][x] = int(round(random.randint(0,1) + ((sum(self.inputInfoY[y]) / self.sizeX) - 0.5)))

    def solve(self):
        while(self.check() == 0):
            self.fillRandom()
            self.printField()

    def check(self):
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
            horizontalSpacing = 1
        else:
            horizontalSpacing = 0

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
            verticalSpacing = 1
        else:
            verticalSpacing = 0

        if horizontalSpacing == 1 and verticalSpacing == 1:
            return 1
        else:
            return 0

print("Starting session.")

gameNumber = 1
startTime = time.time()

input4x4 = [[[2], [2], [3], [1, 2]],
         [[4],
          [3],
          [2],
          [1]
         ]
        ]

input8x8test = [[[8],[6,1],[5,2],[2,2,2],[2],[2],[8],[8]],
[[2],[2],[2],[8],[8],[2,2],[2,2],[8]]]

input8x8 = [[[5],[5],[2],[2],[2],[2],[8],[8]],
[[2],[2],[2],[8],[8],[2,2],[2,2],[2,2]]]

inputInfo = input8x8

size = [len(inputInfo[0]), len(inputInfo[1])]
print("\nInput information:")
print(inputInfo)
print("\nSize:")
print(size)

for x in range(gameNumber):
    NG = Nonogramm(size, inputInfo)
    NG.solveRandom()

    print("\nSolution:")
    NG.printField()

print("\nAverage time:", (time.time() - startTime) / gameNumber, "seconds")



input("\nPress ENTER to exit.")
