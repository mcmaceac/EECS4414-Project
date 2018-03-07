import os
import xlrd
import networkx as nx
import matplotlib.pyplot as plt
import xlwt as xl

countryNameDict = {}
codeFile = "iso3CountryCoordinates.xlsx"

def find_Edges():
    directory = "Export Data/2014"

    wb = xl.Workbook()
    edges = {}
    wb.add_sheet("Edges2015", cell_overwrite_ok=False)
    for filename in os.listdir(directory):
        # print(filename)
        if (not (filename == ".DS_Store")):
            # print("after->" + filename)
            with xlrd.open_workbook(directory + "/" + filename) as workbook:
                current_x1 = ""
                sh = workbook.sheet_by_name('Partner')
                for rownum in range(1, sh.nrows):
                    x1 = sh.cell(rownum, 0).value
                    x2 = sh.cell(rownum, 1).value

                    if (x1 in edges):

                        edges[x1].append(x2)
                    else:
                        edges[x1] = [x2]
    return edges


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