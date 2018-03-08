import os
import xlrd
import xlwt as xl

edges = {}

def main():
    directory = "Export Data/2014"
    # outfile = directory + "/Edges2014"
    # print(directory)
    wb = xl.Workbook()
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

if __name__ == "__main__":
    main()

def get_edges():
    return edges

