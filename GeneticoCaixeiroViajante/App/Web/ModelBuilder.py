from App.Model.Vector import Vector
from App.Model.Edge import Edge
from App.Model.Graph import Graph
from App.Web.RequestData import RequestData
	
def buildModel(json):
	populationSize = json['populationSize']
	mutationRate = json['mutationRate']
	iterationsQuantity = json['iterationsQuantity']
	vectorsNames = json['graphData']['vectors']
	edgesData = json['graphData']['edges']

	vectors = list(map(lambda x: Vector(x) ,vectorsNames))
	def buildEdge(data):		
		def vectorByName(name):
			return list(filter(lambda x:x.name == name,vectors))[0]
		vectorOne = vectorByName(data['vectorOne'])
		vectorTwo = vectorByName(data['vectorTwo'])
		return Edge(vectorOne,vectorTwo, data['weight'])

	edges = list(map(buildEdge,edgesData))
	graph = Graph(edges, vectors)
	return RequestData(populationSize,mutationRate,iterationsQuantity,graph)