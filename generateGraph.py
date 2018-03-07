import os
import xlrd
import networkx as nx
import matplotlib.pyplot as plt

countryNameDict = {}
codeFile = "iso3CountryCoordinates.xlsx"

def generateGraph():
	G = nx.Graph()

	with xlrd.open_workbook(codeFile) as workbook:
		sh = workbook.sheet_by_name('iso3CountryCoordinates')
		for rownum in range(0, sh.nrows):
			nodeName = sh.cell(rownum, 0).value		#iso3 code for the node name
			G.add_node(nodeName, pos=(sh.cell(rownum,2).value, sh.cell(rownum,1).value))

	#for node in G.nodes():
	#	for node2 in G.nodes():
	#		G.add_edge(node, node2)


	positions = nx.get_node_attributes(G, 'pos')
	plt.figure(figsize=(16,8))
	nx.draw(G, positions, node_size = [4 for v in G], with_labels = True)
	plt.show()


def addCodes():
	directory = "Export Data/2014"
	for filename in os.listdir(directory):	#scan every file
		print(filename)
		with xlrd.open_workbook(directory + "/" + filename) as workbook:
			sh = workbook.sheet_by_name('Partner')
			for rownum in range(1, sh.nrows):
				print(sh.cell(rownum,5))

#builds the map that links country names from the world bank data files to their iso3 code (the node name)
def buildCodeMap():	
	with xlrd.open_workbook(codeFile) as workbook:
		sh = workbook.sheet_by_name('iso3CountryCoordinates')
		for rownum in range(0, sh.nrows):
			code = sh.cell(rownum, 0).value
			countryName = sh.cell(rownum, 3).value
			#print(rownum+1, ": " + code + "," + countryName)
			countryNameDict[countryName] = code

#addCodes()
#buildCodeMap()
generateGraph()