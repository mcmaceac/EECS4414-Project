import matplotlib.pyplot as plt
import networkx as nx
import xlrd
import operator

codeFile = "iso3CountryCoordinates.xlsx"
countryInDegrees = {}
countryOutDegrees = {}

def detectCommunities(G):
	pass

#calculates the in and out degree distribution
def degreeDistribution(G):
	with xlrd.open_workbook(codeFile) as workbook:
		sh = workbook.sheet_by_name('iso3CountryCoordinates')
		for rownum in range(0, sh.nrows):
			countryCode = sh.cell(rownum, 0).value		#iso3 code for the node name
			countryInDegrees[countryCode] = G.in_degree(countryCode)
			countryOutDegrees[countryCode] = G.out_degree(countryCode)

	sortedIn = sorted(countryInDegrees.items(), key=operator.itemgetter(1))

	plt.ylabel('In Degree')
	plt.xlabel('Country Code')
	plt.bar(range(len(countryInDegrees)), countryInDegrees.values())
	plt.xticks(range(len(countryInDegrees)), list(countryInDegrees.keys()), rotation=90)
	plt.show()

	plt.ylabel('Out Degree')
	plt.xlabel('Country Code')
	plt.bar(range(len(countryOutDegrees)), countryOutDegrees.values())
	plt.xticks(range(len(countryOutDegrees)), list(countryOutDegrees.keys()), rotation=90)
	plt.show()

def clusteringDistribution(G):
	clust = nx.clustering(G.to_undirected())
	
	plt.ylabel('Clustering Coefficient')
	plt.xlabel('Country Code')
	plt.bar(range(len(clust)), clust.values())
	plt.xticks(range(len(clust)), list(clust.keys()), rotation=90)
	plt.show()

def components(G):
	for comp in nx.strongly_connected_components(G):
		if len(comp) == 1:
			elem = comp.pop()
			print(elem, ": ", G.out_degree(elem))
		else:
			print(comp)

def diameter(G):
	print("Diameter of the SCC: ", nx.diameter(max(nx.strongly_connected_component_subgraphs(G), key=len)))

#method to return the graph with a given filename (adjlist file)
def loadGraph(fileName):
	with open(fileName, "rb") as f:
		G = nx.read_adjlist(f, create_using=nx.DiGraph())
		print("Graph loaded")
	return G

G = loadGraph("WTW.adjlist")
#degreeDistribution(G)
#clusteringDistribution(G)
#components(G)
diameter(G)