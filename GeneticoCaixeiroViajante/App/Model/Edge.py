class Edge(object):
	vectorOne = ''
	vectorTwo = ''
	weight = 0
	def __init__(self, vectorOne, vectorTwo, weight):
		self.vectorOne = vectorOne
		self.vectorTwo = vectorTwo
		self.weight = weight

	def getName(self):
		return self.vectorOne.name + "_to_" + self.vectorTwo.name