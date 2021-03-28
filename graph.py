class Node:
	def __init__(self, point, neighbors = None):
		self.point = point
		self.neighbors = neighbors

	def get_neighbors(self):
		return self.neighbors


"""if __name__ == '__main__':

	graph = Node((1,0)) 
	print(graph.get_neighbors())"""