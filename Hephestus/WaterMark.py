


class WaterMark():
 
    def __init__(self, mark, x, y):

	self.location = {"X": x, "Y" : y}
	self.mark = mark

    def getLocation(self, locationCoords):

	return self.location[locationCoords]

    def getMark(self):

	return self.mark

