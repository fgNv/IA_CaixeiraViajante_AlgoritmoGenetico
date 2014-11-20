from App.Model.Edge import Edge
from App.Model.Vector import Vector

class Graph(object):
	def __init__(self, edges, vectors):
		self.edges = edges
		self.vectors = vectors