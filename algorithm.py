import random
import math
from randompointgenerator import LatLongList


class vertex:
    def __init__(self, xValIn, yValIn):
        self.xVal = xValIn
        self.yVal = yValIn
        self.checked = False


def distance(first, second, vert) :

    xVal = float(vert[first].xVal - vert[second].xVal)
    yVal = float(vert[first].yVal - vert[second].yVal)

    return math.sqrt(math.pow(xVal, 2) + math.pow(yVal, 2))


theWorld = []
numVec = random.randint(3, 101)
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
i = 0
while i < numVec - 1:
    weight += distance(parents[i], parents[i + 1], theWorld)
    i += 1


print(repr(round(weight * 69, 6)) + ' miles')

i = 0
while i < numVec:
    toBePrinted = repr(round(theWorld[parents[i]].xVal, 6)) + ' ' + repr(round(theWorld[parents[i]].yVal, 6))
    print(toBePrinted)
    i += 1



