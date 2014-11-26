import random
from App.Model.Vector import Vector

def genesis(vectors, initialPopulation):

	def buildSolution(vectorsInner):
		result = []
		def buildSolutionInner(remainingVectors):
			if(len(remainingVectors) == 1):
				result.append(remainingVectors[0])
				return

			nextVectorIndex = random.randrange(0, len(remainingVectors))
			nextVector = remainingVectors[nextVectorIndex]
			result.append(nextVector)
			remainingVectorsNext = list(filter(lambda x : x.name != nextVector.name , remainingVectors))			
			buildSolutionInner(remainingVectorsNext)

		buildSolutionInner(vectorsInner)
		return result
		
	initialSolutions = [];
	[initialSolutions.append(buildSolution(vectors)) for x in range(initialPopulation)]
	return initialSolutions	
	