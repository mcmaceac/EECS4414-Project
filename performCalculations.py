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

	plt.bar(range(len(countryInDegrees)), countryInDegrees.values())
	plt.xticks(range(len(countryInDegrees)), list(countryInDegrees.keys()), rotation=90)
	plt.show()

	plt.bar(range(len(countryOutDegrees)), countryOutDegrees.values())
	plt.xticks(range(len(countryOutDegrees)), list(countryOutDegrees.keys()), rotation=90)
	plt.show()

#method to return the graph with a given filename (adjlist file)
def loadGraph(fileName):
	with open(fileName, "rb") as f:
		G = nx.read_adjlist(f, create_using=nx.DiGraph())
		print("Graph loaded")
	return G

G = loadGraph("WTW.adjlist")
degreeDistribution(G)