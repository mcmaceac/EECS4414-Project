import networkx as nx
import matplotlib.pyplot as plt

def generateGraph():
	G = nx.Graph()

	filename = "iso3CountryCoordinates.csv"
	file = open(filename, "r")
	for line in file:
		elmts = [x.strip() for x in line.split(',')]
		nodeName = elmts[0]			#iso3 country code

		G.add_node(nodeName, pos=(float(elmts[3]), float(elmts[2])))

	#for node in G.nodes():
	#	for node2 in G.nodes():
	#		G.add_edge(node, node2)


	positions = nx.get_node_attributes(G, 'pos')
	plt.figure(figsize=(16,8))
	nx.draw(G, positions, node_size = [4 for v in G], with_labels = True)
	plt.show()

generateGraph()