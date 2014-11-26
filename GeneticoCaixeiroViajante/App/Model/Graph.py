from App.Model.Edge import Edge
from App.Model.Vector import Vector

class Graph(object):
	def __init__(self, edges, vectors):
		self.edges = edges
		self.vectors = vectors

	def getEdge(self, vectorOne, vectorTwo):
		item = list(filter(lambda edge: edge.isEquivalent(vectorOne,vectorTwo), self.edges))
		return item[0]