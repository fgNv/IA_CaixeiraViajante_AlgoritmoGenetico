from App.Model.Genesis import genesis
from App.Model.Selection import selectNextGeneration
from App.Model.SolutionItem import SolutionItem

def run(graph, populationSize, mutationRate, iterationsQuantity):
	def getBestSolution(population):
		minFitness = min(list(map(lambda x : x.fitness, population)))
		items = list(filter(lambda x: x.fitness == minFitness, population))
		return items[0]

	population = genesis(graph.vectors,populationSize)
	solutionPopulation = list(map(lambda x: SolutionItem(x, graph), population)) 
	bestSolution = getBestSolution(solutionPopulation)

	historic = []

	for i in range(0, iterationsQuantity):
		historic.append({ "iteration" : i, "solutions" : solutionPopulation})
		population = selectNextGeneration(solutionPopulation, mutationRate)
		solutionPopulation = list(map(lambda x: SolutionItem(x, graph), population)) 
		tempBestSolution = getBestSolution(solutionPopulation)
		if tempBestSolution.fitness < bestSolution.fitness :
			bestSolution = tempBestSolution

	historic.append({ "iteration" : i+1, "solutions" : solutionPopulation})

	return {'bestSolution' : bestSolution, 'historic' : historic}




