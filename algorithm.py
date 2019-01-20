import random
import math
from randompointgenerator import LatLongList

class vertex:
    def __init__(self, xValIn, yValIn):
        self.xVal = xValIn
        self.yVal = yValIn
        self.checked = False


def distance(first, second, vert):
    xVal = float(vert[first].xVal - vert[second].xVal)
    yVal = float(vert[first].yVal - vert[second].yVal)

    return math.sqrt(math.pow(xVal, 2) + math.pow(yVal, 2))

class theTSP:

    theFinal = []
    theWeight = 0

    def __init__(self, numVec):
        theWorld = []
        masterList = LatLongList(numVec)

        i = 0
        while i < numVec:
            theVert = vertex(masterList.l[i][0], masterList.l[i][1])
            theWorld.append(theVert)
            i += 1

        parents = []
        smallest = float("inf")
        index = 0

        i = 2
        while i < numVec:
            dist = distance(i, 0, theWorld)
            if smallest > dist:
                smallest = dist
                index = i
            i += 1

        parents.append(0)
        parents.append(index)

        theWorld[0].checked = True
        theWorld[index].checked = True

        smallest = float("inf")

        i = 1
        while i < numVec:
            if not theWorld[i].checked:
                j = 0
                while j < len(parents) - 1:
                    if smallest >= (distance(parents[j], i, theWorld) + distance(parents[j + 1], i, theWorld) - distance(parents[j], parents[j + 1], theWorld)):
                        smallest = (distance(parents[j], i, theWorld) + distance(parents[j+1], i, theWorld) - distance(parents[j], parents[j+1], theWorld))
                        index = j + 1
                    j += 1
                if smallest < (distance(0, i, theWorld) + distance(parents[len(parents) - 1], i, theWorld) - distance(0, parents[len(parents) - 1], theWorld)):
                    parents.insert(index, i)
                else:
                    parents.append(i)
                theWorld[i].checked = True

            smallest = float("inf")
            i += 1

        weight = float(distance(parents[0], parents[numVec - 1], theWorld))

        heaviestDist = weight
        heaviestNum = numVec - 1

        i = 0
        while i < numVec - 1:
            if distance(parents[i], parents[i + 1], theWorld) > heaviestDist:
                heaviestDist = distance(parents[i], parents[i + 1], theWorld)
                heaviestNum = i
            weight += distance(parents[i], parents[i + 1], theWorld)
            i += 1

        # print(repr(round(weight * 69, 6)) + ' miles')
        weight -= heaviestDist
        self.theWeight = weight * 69

        '''
        i = 0
        while i < numVec:
            toBePrinted = repr(round(theWorld[parents[i]].xVal, 6)) + ' ' + repr(round(theWorld[parents[i]].yVal, 6))
            print(toBePrinted)
            i += 1
        '''

        i = heaviestNum + 1
        while i < numVec:
            self.theFinal.append((theWorld[parents[i]].xVal, theWorld[parents[i]].yVal))
            i += 1

        i = 0
        while i < heaviestNum + 1:
            self.theFinal.append((theWorld[parents[i]].xVal, theWorld[parents[i]].yVal))
            i += 1

    def getList(self):
        return self.theFinal

    def getWeight(self):
        return self.theWeight


# For printing/testing purposes
#
# driver = theTSP(10)
#
# driver.run()
# print(driver.getWeight())
# i = 0
# while i < len(driver.getList()):
#         toBePrinted = repr(round(driver.getList()[i][0], 6)) + ' ' + repr(round(driver.getList()[i][1], 6))
#         print(toBePrinted)
#         i += 1
