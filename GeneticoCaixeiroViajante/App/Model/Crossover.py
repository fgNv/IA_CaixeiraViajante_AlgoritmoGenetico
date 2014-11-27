import random
from functools import reduce

def mutate(child):
	firstIndex = random.randrange(0, len(child))
	secondIndex = random.randrange(0, len(child))
	while(firstIndex == secondIndex):
		secondIndex = random.randrange(0, len(child))

	temp = child[firstIndex]
	child[firstIndex] = child[secondIndex]
	child[secondIndex] = temp
	return child

def crossover(first,second, mutationRate):
	def makeCorrections(solution):
		def isTaken(value, collection):
			filtered = list(filter(lambda x: x.name == value.name, collection))	
			return len(filtered) > 0;

		untaken = list(filter(lambda x: not isTaken(x, solution), first))

		if(len(untaken) == 0):
			return solution

		result = []	
		for i in range(0, len(solution)):
			if(isTaken(solution[i], result)):
				result.append(untaken.pop())
			else:
				result.append(solution[i])

		return result		

	def generateChild(one, two, cutPoint):
		for i in range(0,cutPoint):
			yield one[i]

		for i in range(cutPoint,len(one)):
			yield two[i]
	
	def raffleMutation(child):
		if(mutationRate == 0):
			return child
		mutationRand = random.randrange(0,100)		
		if(mutationRand <= mutationRate ):
			return mutate(child)
		return child

	totalVertexes = len(first)
	cutPoint = random.randrange(0,totalVertexes)

	yield raffleMutation(makeCorrections(list(generateChild(first,second,cutPoint))))	
	yield raffleMutation(makeCorrections(list(generateChild(second,first,cutPoint))))
