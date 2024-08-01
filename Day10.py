apple = 'Mango'

# for char in apple:
#   print(char)

# for i in range(0, len(apple)):
#   print(apple[i])


#slicing in string

print(apple[0:4]) #including 0th index and excluding 4th index
print(apple[1:4]) #including 1st index and excluding 4th index
print(apple[-3:-1]) #including -3rd index and excluding -1st index
'''
Python will do the following:
  apple[-3:-1]
  1. len(apple) - 3 = 5 - 3 = 2
  2. len(apple) - 1 = 5 - 1 = 4
  3. apple[2:4] = 'ng'
'''

# quick quiz:
nm = "siddesh"

print(nm[-4:-2])  #de
