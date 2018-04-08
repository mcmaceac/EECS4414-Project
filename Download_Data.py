import requests
import xlrd
import os
import urllib
from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup



link_begin = "https://wits.worldbank.org/Download.aspx?Reporter="
link_middle = "&Year="
link_end = "&Tradeflow=Export&Partner=ALL&Product=Total&Type=Product&Lang=en"
link = "a"
f = ""
def getAllPartnersData(year):
     with open("CountryCodes.txt", "r") as countries:
          for country in countries:

               country = country.rstrip('\n')
               link = link_begin + country + link_middle + year + link_end
               print(link)
               try:
                    f = urllib.request.urlopen(link)

               except:
                    print(country + " not found")
                    pass

               if(not f == ""):
                    with open(country + ".xlsx", "wb") as code:
                         code.write(f.read())
               link = "";
def getProductExporOrImportData(year, type):
     f = ""
     with open("CountryCodes.txt", "r") as countries:
          for country in countries:
               country = country.rstrip('\n')
               with open("Products.txt", "r") as links:
                    for link in links:

                         link = link.replace("{1}", country)
                         link = link.replace("{2}", year)
                         link = link.replace("{3}", type)
                         link = link.rstrip('\n')
                         print("new->" + link)
                         try:
                              f = urllib.request.urlopen(link)

                         except:
                              print(country + " not found")
                              pass
                         if (not f == ""):
                              path = year + "/"+country+"/"
                              if not os.path.exists(path):
                                   os.makedirs(path)
                              try:
                                   startIndex = link.index("_")
                                   endIndex = link.index("&", startIndex)
                                   product = link[startIndex+1:endIndex]
                              except:
                                   product = "AgrRaw"
                              print("product->" + product)
                              with open(path + country +"-"+product + ".xlsx", "wb") as code:
                                   code.write(f.read())
                         link = "";
year = "2010"
type = "export"
# getProductExporOrImportData(year, type)
getAllPartnersData(year)