class RequestData(object):
	populationSize = 0
	mutationRate = 0
	iterationsQuantity = 0
	graph = 0
	selectionStrategy = ''

	def __init__(self, populationSize, mutationRate, iterationsQuantity, graph, selectionStrategy):
		self.populationSize = populationSize
		self.mutationRate = mutationRate
		self.iterationsQuantity = iterationsQuantity
		self.graph = graph
		self.selectionStrategy = selectionStrategy
	