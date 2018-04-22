import matplotlib.pyplot as plt
import networkx as nx
from networkx.algorithms.community.centrality import girvan_newman
from networkx import edge_betweenness_centrality as betweenness
import xlrd
import operator
from operator import itemgetter
import itertools

codeFile = "iso3CountryCoordinates.xlsx"
countryInDegrees = {}
countryOutDegrees = {}
countryCodeDict = {}

def detectCommunities(G):
	k = 7 #7 continents
	comp = girvan_newman(G, most_valuable_edge=heaviest)
	limited = itertools.takewhile(lambda c: len(c) <= k, comp)
	for communities in limited:
		print(tuple(sorted(c) for c in communities))

def most_central_edge(G):
	centrality = betweenness(G, weight='weight')
	#return max(centrality, key=centrality.get)
	return sorted(centrality, key=centrality.get, reverse=True)[:5]

def top_pagerank(G):
	ranks = nx.pagerank(G)
	return sorted(ranks, key=ranks.get, reverse=True)[:5]

def heaviest(G):
	u, v, w = max(G.edges(data='weight'), key=itemgetter(2))
	return (u, v)


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

def nodeDegrees(G):
	with xlrd.open_workbook(codeFile) as workbook:
		sh = workbook.sheet_by_name('iso3CountryCoordinates')
		for rownum in range(0, sh.nrows):
			countryCode = sh.cell(rownum, 0).value		#iso3 code for the node name
			print(countryCodeDict[countryCode], "+", G.in_degree(countryCode), "+", G.out_degree(countryCode))

def clusteringDistribution(G):
	clust = nx.clustering(G.to_undirected())
	
	plt.ylabel('Clustering Coefficient')
	plt.xlabel('Country Code')
	plt.bar(range(len(clust)), clust.values())
	plt.xticks(range(len(clust)), list(clust.keys()), rotation=90)
	plt.show()

def clusteringByNode(G):
	clust = nx.clustering(G.to_undirected())
	for code in clust.keys():
		print(countryCodeDict[code], "+", clust[code])


def components(G):
	for comp in nx.strongly_connected_components(G):
		if len(comp) == 1:
			elem = comp.pop()
			print(elem, ": ", G.out_degree(elem))
		else:
			print(comp)

def diameter(G):
	print("Diameter of the SCC: ", nx.diameter(max(nx.strongly_connected_component_subgraphs(G), key=len)))

def SCC(G):
	for subgraph in nx.strongly_connected_components(G):
		print(subgraph)

def getEdgeData(G):
	print(G.edges(data=True))

#method to return the graph with a given filename (adjlist file)
def loadGraph(fileName):
	with open(fileName, "rb") as f:
		if fileName.find("edgelist") == -1:
			G = nx.read_adjlist(f, create_using=nx.DiGraph())
			print("Graph loaded from adjlist")
		else:
			G = nx.read_edgelist(f, data=(('weight', float),), create_using=nx.DiGraph())
			print("Graph " + fileName + " loaded from edgelist")
	return G

def buildCodeMap():	
	with xlrd.open_workbook(codeFile) as workbook:
		sh = workbook.sheet_by_name('iso3CountryCoordinates')
		for rownum in range(0, sh.nrows):
			code = sh.cell(rownum, 0).value
			countryName = sh.cell(rownum, 3).value
			#print(rownum+1, ": " + code + "," + countryName)
			countryCodeDict[code] = countryName

#G = loadGraph("WTW.adjlist")

years = ["2006", "2007", "2008", "2009", "2010", "2011", "2012", "2013", "2014", "2016"]

for year in years:
	G = loadGraph("graphs/WTW" + year + ".edgelist")
	#print(G["CAN"]["USA"]['weight'])
	#print(most_central_edge(G))
	print(top_pagerank(G))
	print(G.size(weight='weight'))

#degreeDistribution(G)
buildCodeMap()
#nodeDegrees(G)
#clusteringByNode(G)
#clusteringDistribution(G)
#components(G)

#detectCommunities(G)
#getEdgeData(G)
#SCC(G)