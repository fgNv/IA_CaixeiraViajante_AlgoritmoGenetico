from Tests.FitnessTest import FitnessTest
from Tests.GenesisTests import printSolution
from App.Model.Genesis import genesis
from App.Model.SolutionItem import SolutionItem
from App.Model.Selection import selectNextGeneration
from App.Model.Selection import getDuplicates
from App.Model.Vector import Vector

class SelectionTest(object):
	def run(self):
		fitnessTest = FitnessTest()
		sampleGraph = fitnessTest.getSampleGraph()

		initialPopulation = 3
		initialSolutions = genesis(sampleGraph.vectors, initialPopulation)
		solutionItems = list(map(lambda i : SolutionItem(i,sampleGraph), initialSolutions))
		print('----Selection tests-----\n')
		nextGen = selectNextGeneration(solutionItems, 0)
		[printSolution(result) for result in initialSolutions]
		print('\n')	
		[printSolution(result) for result in nextGen]
		print('\n')

	def checkDuplicates(self):
		vecA = Vector('a')
		vecB = Vector('b')
		vecC = Vector('c')
		samplePopulation = [[vecA, vecB, vecC], [vecA, vecC, vecB], [vecA, vecB, vecC]]
		print('----Check Duplicates tests-----\n')
		duplicates = list(getDuplicates(samplePopulation))
		print(duplicates )


