#Tupel
# -> Tuple is immutable and cannot be canged

tup = (1, ) # if we want to give only one element in tuple then we should provide one comma at the last of the tuple so that python can understand that it's a tupel not a int, otherwise it will interprate it as int

tup1 = ('sid', 1, True, -1.4)

print(type(tup1), tup1)

print(tup1[0], tup1[1])

if 3421 in tup:
  print('exist')
else:
  print('Not exist')


tup2 = tup1[1:4]
print(f"==>> tup2: {tup2}")


