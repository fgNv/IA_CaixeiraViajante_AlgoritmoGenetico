from App.Model.Edge import Edge
from App.Model.Vector import Vector
from App.Model.Graph import Graph
from App.Model.Genesis import *
from Tests.GenesisTests import *
from App.Model.Fitness import *

class FitnessTest(object):
	def getSampleGraph(self):
		vecA = Vector('a')
		vecB = Vector('b')
		vecC = Vector('c')
		vecD = Vector('d')

		vectors = [vecA, vecB, vecC, vecD]

		edges = [Edge(vecA,vecB,3), Edge(vecA,vecC,5), Edge(vecA,vecD,7), 
				 Edge(vecB,vecC,8), Edge(vecB,vecD,4), 
				 Edge(vecC,vecD,5),
				 Edge(vecB,vecA,3), Edge(vecC,vecA,5), Edge(vecD,vecA,7), 
				 Edge(vecC,vecB,8), Edge(vecD,vecB,4), 
				 Edge(vecD,vecC,5) ]

		return Graph(edges, vectors)

	def run(self):
		print('----Fitness tests-----\n')
		sampleGraph = self.getSampleGraph()

		initialPopulation = 3
		initialSolutions = genesis(sampleGraph.vectors, initialPopulation)

		printSolution(initialSolutions[0])
		solutionEdges = getSolutionEdges(initialSolutions[0],sampleGraph)

		edgePrint = lambda acc,i: acc + 'from:' + i.vectorOne.name + ' to:' + i.vectorTwo.name + ' weight:' + str(i.weight) + '\n'
		print(reduce(edgePrint,solutionEdges,''))

		print(calculateFitness(initialSolutions[0],sampleGraph))
		print('\n')