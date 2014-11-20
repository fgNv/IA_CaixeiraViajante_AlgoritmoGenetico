from App.Model.Edge import Edge

class Fitness(object):
	def calculate(self, edges):
		weights = map(lambda e : e.weight, edges)
		return reduce(lambda x,y : x + y, weights)