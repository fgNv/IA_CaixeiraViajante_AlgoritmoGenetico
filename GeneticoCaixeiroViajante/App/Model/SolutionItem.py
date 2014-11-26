from App.Model.Fitness import calculateFitness

class SolutionItem(object):
	fitness = 0
	solution = ''

	def __init__(self, solution, graph):
		self.solution = solution
		self.fitness = calculateFitness(solution,graph)