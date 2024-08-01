#Tuple methods


#changes in tuple
countries = ("India", "Spain", "Italy", "England", "Germany")

temp = list(countries)
temp.append("Russia")

temp.pop(3)
temp[2] = "Finland"
countries = tuple(temp)
print(countries)

#merging 
countries1 = ('a', 'b', 'c')
tCountries = countries + countries1
print(f"==>> tCountries: {tCountries}")

res = tCountries.index('a')
print(f"==>> res: {res}")

res = len(countries)
print(f"==>> res: {res}")
