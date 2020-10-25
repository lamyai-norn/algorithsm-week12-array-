def getIndexOfCountry(countryName):
  for index in range(len(countryNames)):
     if countryNames[index]==countryName:
        return index
  return -1
countryNames=["canada","france","usa","cambodia"]
countryPopulationMillions=[110,70,250,8]
countryName=input("Enter country: ")
indexOfCountry=getIndexOfCountry(countryName)
if indexOfCountry==-1:
    print("wrong country")
else:
    print("Population of "+countryName+" is " + str(countryPopulationMillions[indexOfCountry])+" millions people")

