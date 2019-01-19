import random
random.seed()

class LatLongList:
    def __init__(self):
        self.l = []
        for x in range(10):
            self.l.append((random.uniform(42.711747, 42.74863), random.uniform(-84.483571, -84.493784)))

    def getlist(self):
        return self.l


pointslist = LatLongList()
li = pointslist.getlist()
print(li)

