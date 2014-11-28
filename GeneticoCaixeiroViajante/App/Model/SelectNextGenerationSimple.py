from App.Model.Crossover import crossover
from App.Model.Crossover import mutate
from functools import reduce
from App.Model.RoulleteSelection import getDuplicates
from App.Model.Crossover import mutate

def selectNextGenerationSimple(currentGeneration, mutationRate, crossData):
	nextGeneneration = []
	replicatedGeneration = currentGeneration

	populationSize = len(currentGeneration)
	currentCross = 0

	while(len(nextGeneneration) < populationSize):
		if not any(replicatedGeneration):
			replicatedGeneration = currentGeneration

		minFitness = min(map(lambda x:x.fitness,replicatedGeneration))
		first = list(filter(lambda x: x.fitness == minFitness,replicatedGeneration))[0]

		replicatedGeneration = list(filter(lambda x: x.fitness != minFitness,replicatedGeneration))

		if not any(replicatedGeneration):
			replicatedGeneration = currentGeneration		

		minFitness = min(map(lambda x:x.fitness,replicatedGeneration))
		second = list(filter(lambda x: x.fitness == minFitness,replicatedGeneration))[0]

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


