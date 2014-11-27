
from App.Model.Runner import run
from Tests.FitnessTest import FitnessTest

class RunnerTest(object):
	def run(self):

		fitnessTest = FitnessTest()
		sampleGraph = fitnessTest.getSampleGraph()
		populationSize = 3
		mutationRate = 15
		iterationsQuantity = 10
		result = run(sampleGraph, populationSize, mutationRate, iterationsQuantity)
		print(result)