import requests
import xlrd
import urllib
from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup


year = "2008"
link_begin = "https://wits.worldbank.org/Download.aspx?Reporter="
link_middle = "&Year="
link_end = "&Tradeflow=Export&Partner=ALL&Product=Total&Type=Product&Lang=en"
link = "a"
f = ""

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