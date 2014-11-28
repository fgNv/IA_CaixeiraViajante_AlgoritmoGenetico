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

def roulleteSelectNextGeneration(currentGeneration, mutationRate, crossData):

	maxFitness = max(map(lambda x: x.fitness, currentGeneration))

	def getItemsRange():			
		def calculateIndex(dictionary, item):
			acummulatedIndexes = sum(dictionary.keys())
			result = abs(item.fitness - maxFitness - 1) + acummulatedIndexes
			return result

		dic = {}
		for item in currentGeneration:
			dic.update({calculateIndex(dic,item) : item })

		return dic

	itemsRange = getItemsRange()
	nextGeneneration = []
	maxIndex = max(itemsRange.keys())
	populationSize = len(currentGeneration)
	total = reduce(lambda acc,i: acc + i.fitness, currentGeneration, 0)

	currentCross = 0
	while(len(nextGeneneration) < populationSize):
		randomNumber = random.randrange(0, maxIndex)
		def getIndexFilter(randomValue):
			keysGreaterThan = filter(lambda i: i >= randomValue, itemsRange.keys());
			return min(keysGreaterThan);

		oppositeRandom = randomNumber + (maxIndex/2)
		if oppositeRandom > maxIndex:
			oppositeRandom = oppositeRandom - maxIndex + 1

		index = getIndexFilter(randomNumber)		
		oppositeIndex = getIndexFilter(oppositeRandom)		
		first = itemsRange[index]		
		second = itemsRange[oppositeIndex]
		
		crossResult = crossover(list(first.solution), list(second.solution), mutationRate)
		addedItem = next(crossResult)
		nextGeneneration.append(addedItem)
		addedItems = []
		addedItems.append(addedItem)
		
		if(len(nextGeneneration) < populationSize):
			addedItem = next(crossResult)
			nextGeneneration.append(addedItem)
			addedItems.append(addedItem)
		
		crossData.append({"crossNumber" : currentCross, "first" : first, "second" : second, "addedItems" : addedItems })
		currentCross += 1

	duplicatedIndexes = getDuplicates(nextGeneneration)
	while len(list(duplicatedIndexes)) > 0:	
		duplicatedIndexes = list(getDuplicates(nextGeneneration))
		for i in range(0, len(duplicatedIndexes)) :
			nextGeneneration[duplicatedIndexes[i]] = mutate(nextGeneneration[duplicatedIndexes[i]])

	return nextGeneneration