class RequestData(object):
	populationSize = 0
	mutationRate = 0
	iterationsQuantity = 0
	graph = 0

	def __init__(self, populationSize, mutationRate, iterationsQuantity, graph):
		self.populationSize = populationSize
		self.mutationRate = mutationRate
		self.iterationsQuantity = iterationsQuantity
		self.graph = graph
	