from App.Model.Runner import run
from Tests.FitnessTest import FitnessTest
from App.Model.SelectNextGenerationSimple import selectNextGenerationSimple

class RunnerTest(object):
	def run(self):

		fitnessTest = FitnessTest()
		sampleGraph = fitnessTest.getSampleGraph()
		populationSize = 3
		mutationRate = 15
		iterationsQuantity = 10
		result = run(sampleGraph, populationSize, mutationRate, iterationsQuantity, selectNextGenerationSimple)
		#print(result)