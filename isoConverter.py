import pycountry

fo = open("iso3CountryCoordinates.csv", "w+")
with open("countryCoordinates.csv", "r") as f:
	for line in f.readlines():
		country = line.split(',')
		iso2 = country[0]

		pyCountry = pycountry.countries.get(alpha_2=iso2)
		iso3Line = pyCountry.alpha_3 + "," + line
		fo.write(iso3Line)
fo.close()