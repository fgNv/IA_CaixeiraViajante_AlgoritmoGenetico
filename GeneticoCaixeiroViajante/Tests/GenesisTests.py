from App.Model.Genesis import Genesis
from App.Model.Vector import Vector
from App.Model.Edge import Edge
from functools import reduce

class GenesisTests(object):	
	def generateEdges(self, vectors):
		edges = []
		def addEdge(v1,v2):
			if(v1.name != v2.name):
				edges.append(Edge(v1,v2,1))			

		[[addEdge(v1,v2) for v1 in vectors] for v2 in vectors]
		return edges


	def getInitialPopulationSample(self, initialPopulation):
		genesis = Genesis()
		vectors = [Vector('a'), Vector('b'), Vector('c'), Vector('d'), Vector('e'), Vector('f'), Vector('g')]
		edges = self.generateEdges(vectors)

		print(len(edges))
		results = genesis.Begin(edges, initialPopulation)
		return results;

	def run(self):
		def printResults(results, initialPopulation):
			def printItem(item):
				itemNames = map(lambda x : x.getName(), item)
				itemNamesStr = reduce(lambda x,y: x + ' -> ' + y , itemNames)
				print(itemNamesStr)

			[printItem(result) for result in results]
			if(len(results) == initialPopulation):
				print("Genesis - ok")
			else:
				print("Genesis - unexpected initial population size")

		initialPopulation = 3
		results = self.getInitialPopulationSample(initialPopulation)
		printResults(results, initialPopulation)		