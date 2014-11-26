from App.Model.Genesis import *
from App.Model.Vector import Vector
from functools import reduce

def printSolution(item):
	itemNamesStr = reduce(lambda x,y: x + ' -> ' + y.name , item, '')
	print(itemNamesStr)

class GenesisTests(object):	
	def getInitialPopulationSample(self, initialPopulation):
		vectors = [Vector('a'), Vector('b'), Vector('c'), Vector('d'), Vector('e'), Vector('f'), Vector('g')]

		solutions = genesis(vectors, initialPopulation)
		return solutions;

	def run(self):
		def printResults(solutions, initialPopulation):		
			[printSolution(result) for result in solutions]
			if(len(solutions) == initialPopulation):
				print("Genesis - ok")
			else:
				print("Genesis - unexpected initial population size")

		print('----Genesis tests-----\n')
		initialPopulation = 3
		solutions = self.getInitialPopulationSample(initialPopulation)
		printResults(solutions, initialPopulation)	
		print('\n')	