import random
from App.Model.Edge import Edge

class Genesis(object):
	def Begin(this, edges, initialPopulation):		
		
		def buildSolution(result, remainingEdges):
			if(len(remainingEdges) == 1):
				result.append(remainingEdges[0])
				return result

			nextEdgeIndex = random.randrange(0, len(remainingEdges))
			nextEdge = remainingEdges[nextEdgeIndex]
			result.append(nextEdge)
			remainingEdgesNext = list(filter(lambda x : x.getName() != nextEdge.getName() , remainingEdges))			
			return buildSolution(result, remainingEdgesNext)

		results = [];
		[results.append(buildSolution([], edges)) for x in range(initialPopulation)]
		return results		