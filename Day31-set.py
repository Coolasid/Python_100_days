# For removing set elements, we use set
#set are the unorders data collections

s = {2, 3, 5, 2, 4}

print(s)

sid = {} # this is not the correct way to write a empty set, python takes it as a dictonary
sid = set() # this is correct way
print(f"==>> sid: {type(sid)}")

# for value in s:
#     print(value)



#operatins on set

s2 = {3, 6, 7, 5}

print(s.union(s2)) # here values of s and s2 dosent changes
s.update(s2) # but if we want to change the value of s then we can use update


cities = {'Tokyo', 'Madrid', 'Berlin', "Delhi"}
cities2 = {'Tokyo', 'Seoul', 'Kabul', "Madrid"}

cities3 = cities.intersection(cities2)
citiesU = {'Tokyo', 'Madrid', 'Berlin', "Delhi"}
citiesU.intersection_update(cities2)
print(f"==>> cities3: {cities3}") # {"Madrid", "Tokyo"} only common elements are present

cities4 = cities.symmetric_difference(cities2)
print(f"==>> cities4: {cities4}")  # {'Kabul', 'Delhi', 'Seoul', 'Berlin'} in this common element get elemanited
citiesU = {'Tokyo', 'Madrid', 'Berlin', "Delhi"}
citiesU.symmetric_difference_update(cities2)


cities5 = cities.difference(cities2)
print(f"==>> cities5: {cities5}") # {'Berlin', 'Delhi'} elements which are present in cities but not in cities2, like cities - cities2
citiesU = {'Tokyo', 'Madrid', 'Berlin', "Delhi"}
citiesU.difference_update(cities2)


print(cities.isdisjoint(cities2)) # returns true if the intersection of set is zero means they are not joint 



cities = {'Tokyo', 'Madrid', 'Berlin', "Delhi"}
cities2 = {'Seoul', 'Kabul'}
print(cities.issuperset(cities2))
cities3 = {'Berlin', 'Madrid', "Delhi"}
print(cities.issuperset(cities3))


# to remove element from the set
cities.remove('Tokyo') 
print(f"==>> cities: {cities}")
cities.discard('Tokyo2')
print(f"==>> cities: {cities}")
#** The main diff bt remove and discard is that discard does not give error when it find zero item to discard but remove gives us error 


cities = {'Tokyo', 'Madrid', 'Berlin', "Delhi"}
item = cities.pop() # it poput the last element but our set is unordered so we can't specify which element is present in last.
print(f"==>> item: {item}")

del cities  #delete whole cities and it is not accessable

cities = {'Tokyo', 'Madrid', 'Berlin', "Delhi"}
cities.clear() #clear the set not delete whole set  gives empty set
print(f"==>> cities: {cities}")

cities = {'Tokyo', 'Madrid', 'Berlin', "Delhi"}

if 'Tokyo' in cities:
    print('Tokyo is present')
else:
    print('Tokyo is absent.')


