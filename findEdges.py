import os
import xlrd

def addCodes():
	directory = "Export Data/2014"
	for filename in os.listdir(directory):	#scan every file
		print(filename)
		with xlrd.open_workbook(directory + "/" + filename) as workbook:
			sh = workbook.sheet_by_name('Partner')
			for rownum in range(1, sh.nrows):
				print(sh.cell(rownum,5))			

addCodes()