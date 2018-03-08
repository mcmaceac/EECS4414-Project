import os
import xlrd
import networkx as nx
import matplotlib.pyplot as plt

countryNameDict = {}
codeFile = "iso3CountryCoordinates.xlsx"

def generateGraph():
	G = nx.DiGraph()

	with xlrd.open_workbook(codeFile) as workbook:
		sh = workbook.sheet_by_name('iso3CountryCoordinates')
		for rownum in range(0, sh.nrows):
			nodeName = sh.cell(rownum, 0).value		#iso3 code for the node name
			G.add_node(nodeName, pos=(sh.cell(rownum,2).value, sh.cell(rownum,1).value))

	addEdges(G)

	positions = nx.get_node_attributes(G, 'pos')
	plt.figure(figsize=(16,8))
	nx.draw(G, positions, node_size = [4 for v in G], with_labels = True)
	
	for code in countryNameDict.values():
		printDegrees(G, code)
	plt.show()


def addEdges(G):
	directory = "Export Data/2014"
	for filename in os.listdir(directory):
		with xlrd.open_workbook(directory + "/" + filename) as workbook:
			sh = workbook.sheet_by_name('Partner')
			for rownum in range(1, sh.nrows):
				exporter = sh.cell(rownum, 0).value
				partner = sh.cell(rownum, 1).value

				if exporter in countryNameDict and partner in countryNameDict:	#only add the edge if it is a valid country
					u = countryNameDict[exporter]		#exporter
					v = countryNameDict[partner]		#partner
					edgeWeight = sh.cell(rownum, 5).value
					G.add_edge(u, v, weight=edgeWeight)


#builds the map that links country names from the world bank data files to their iso3 code (the node name)
def buildCodeMap():	
	with xlrd.open_workbook(codeFile) as workbook:
		sh = workbook.sheet_by_name('iso3CountryCoordinates')
		for rownum in range(0, sh.nrows):
			code = sh.cell(rownum, 0).value
			countryName = sh.cell(rownum, 3).value
			#print(rownum+1, ": " + code + "," + countryName)
			countryNameDict[countryName] = code

def printDegrees(G, countryCode):
	inDegree = G.in_degree(countryCode)
	outDegree = G.out_degree(countryCode)

	print("[",countryCode,"] out: ", outDegree, " in: ", inDegree)

buildCodeMap()
generateGraph()