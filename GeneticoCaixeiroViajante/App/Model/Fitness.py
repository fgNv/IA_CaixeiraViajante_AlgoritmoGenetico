from App.Model.Edge import Edge
from App.Model.Graph import Graph
from functools import reduce

def getSolutionEdges(solution, graph):	
	solutionEdges = []
	initialVector = solution[0]

	def getSolutionEdgesInner(innerSolution):	
		if(len(innerSolution) == 1):
			solutionEdges.append(graph.getEdge(innerSolution[0], initialVector)) 
			return

		solutionEdges.append(graph.getEdge(innerSolution[0], innerSolution[1])) 
		nextSolution = list(filter(lambda x: x.name != innerSolution[0].name, innerSolution))	
		getSolutionEdgesInner(nextSolution)

	getSolutionEdgesInner(solution)
	return solutionEdges

def calculateFitness(solution, graph):
	solutionEdges = getSolutionEdges(solution, graph)
	return reduce(lambda x,y : x + y.weight, solutionEdges, 0)