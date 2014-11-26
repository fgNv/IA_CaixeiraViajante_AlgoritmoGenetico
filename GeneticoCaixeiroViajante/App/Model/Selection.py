from functools import reduce
import random
from App.Model.Crossover import crossover
from App.Model.Crossover import mutate

def getDuplicates(generation):
	checked = []
	index = 0
	for item in generation:
		key = reduce(lambda acc,i:acc + i.name + "->", item,"")	
		if(len(list(filter(lambda x: x == key, checked))) > 0):
			yield index 				
		else:
			checked.append(key)
		index = 1 + index

def selectNextGeneration(currentGeneration, mutationRate):

	def getItemsRange():			
		def calculateIndex(dictionary, item):
			acummulatedIndexes = sum(dictionary.keys())
			result = item.fitness + acummulatedIndexes
			return result

		dic = {}
		for item in currentGeneration:
			dic.update({calculateIndex(dic,item) : item })

		return dic

	itemsRange = getItemsRange()
	nextGeneneration = []
	populationSize = len(currentGeneration)
	total = reduce(lambda acc,i: acc + i.fitness, currentGeneration, 0)

	while(len(nextGeneneration) < populationSize):
		randomNumber = random.randrange(0, total)
		def getIndexFilter(randomValue):
			keysGreaterThan = filter(lambda i: i > randomValue, itemsRange.keys());
			return min(keysGreaterThan);

		oppositeRandom = abs(randomNumber - total/2)
		index = getIndexFilter(randomNumber)		
		oppositeIndex = getIndexFilter(oppositeRandom)		
		first = itemsRange[index]		
		second = itemsRange[oppositeIndex]

		crossResult = crossover(list(first.solution), list(second.solution), mutationRate)
		nextGeneneration.append(next(crossResult))
		if(len(nextGeneneration) < populationSize):
			nextGeneneration.append(next(crossResult))

	duplicatedIndexes = getDuplicates(nextGeneneration)
	while len(list(duplicatedIndexes)) > 0:	
		duplicatedIndexes = list(getDuplicates(nextGeneneration))
		for i in range(0, len(duplicatedIndexes)) :
			nextGeneneration[duplicatedIndexes[i]] = mutate(nextGeneneration[duplicatedIndexes[i]])

	return nextGeneneration