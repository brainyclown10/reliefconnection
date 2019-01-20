import random
random.seed()


class LatLongList:
    def __init__(self, num):
        self.l = []
        for x in range(num):
            self.l.append((random.uniform(42.711747, 42.74863), random.uniform(-84.483571, -84.493784)))

    def getlist(self):
        return self.l


# For testing purposes
# pointslist = LatLongList(10)
# li = pointslist.getlist()
# print(li)

