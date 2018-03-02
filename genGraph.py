import networkx as nx
import matplotlib.pyplot as plt

def generateGraph():
	G = nx.Graph()

	filename = "countryCoordinates.csv"
	file = open(filename, "r")
	for line in file:
		elmts = [x.strip() for x in line.split(',')]
		nodeName = elmts[0]

		G.add_node(nodeName, pos=(float(elmts[2]), float(elmts[1])))

	#for node in G.nodes():
	#	for node2 in G.nodes():
	#		G.add_edge(node, node2)


	positions = nx.get_node_attributes(G, 'pos')
	plt.figure(figsize=(10,10))
	nx.draw(G, positions, node_size = [4 for v in G], with_labels = True)
	plt.show()

generateGraph()